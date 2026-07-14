import pyray as pr


objects = []


GRAVITY = 600


class GameObject:

    def __init__(self, x, y, w=16, h=16, color=pr.RED):

        self.x = x
        self.y = y

        self.w = w
        self.h = h

        self.vx = 0
        self.vy = 0

        self.mass = 1

        self.color = color

        self.alive = True


    def rect(self):

        return pr.Rectangle(
            self.x,
            self.y,
            self.w,
            self.h
        )



def spawn_object(x, y):

    obj = GameObject(
        x,
        y,
        20,
        20,
        pr.RED
    )

    objects.append(obj)

    return obj



def destroy_object(obj):

    if obj in objects:
        objects.remove(obj)




def solid_at(world,x,y):

    tx = int(x / 4)
    ty = int(y / 4)

    if ty < 0 or tx < 0:
        return True

    if ty >= len(world):
        return True

    if tx >= len(world[0]):
        return True


    # stone only
    return world[ty][tx] == 4




def update_objects(world,dt):


    for obj in objects:


        # gravity

        obj.vy += GRAVITY * dt


        # X movement

        obj.x += obj.vx * dt


        if solid_at(
            world,
            obj.x,
            obj.y
        ):

            obj.x -= obj.vx * dt
            obj.vx = 0



        # Y movement

        obj.y += obj.vy * dt


        if solid_at(
            world,
            obj.x,
            obj.y + obj.h
        ):


            obj.y -= obj.vy * dt

            obj.vy = 0



        # friction

        obj.vx *= 0.8



def draw_objects():

    for obj in objects:

        pr.draw_rectangle_rec(
            obj.rect(),
            obj.color
        )



def push_material(world,obj):

    """
    Object interaction with sand/water
    """

    left = int(obj.x / 4)
    right = int((obj.x+obj.w)/4)

    top = int(obj.y/4)
    bottom = int((obj.y+obj.h)/4)



    for y in range(top,bottom+1):

        for x in range(left,right+1):

            if 0 <= y < len(world) and 0 <= x < len(world[0]):

                tile = world[y][x]


                # object pushes sand

                if tile == 2:

                    if y > 0:

                        world[y][x] = 0

                        world[y-1][x] = 2



                # water disappears under object

                elif tile == 3:

                    world[y][x] = 0