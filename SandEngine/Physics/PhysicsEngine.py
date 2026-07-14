# MATERIAL PHYSICS
# handles sand, water and other tile behaviors
from SandEngine.Libs import *

# ===== MATERIAL IDS =====

AIR = 0
SAND = 2
WATER = 3
STONE = 4
GRAVIY = 5

# ===== MAP SIZE =====

MAP_W = 256
MAP_H = 256



# ===== HELPERS =====

def inside(x, y):
    return 0 <= x < MAP_W and 0 <= y < MAP_H



def swap(world, x1, y1, x2, y2):

    world[y1][x1], world[y2][x2] = (
        world[y2][x2],
        world[y1][x1]
    )



# ===== SAND =====

def update_sand(world, x, y):

    row = world[y]
    below = world[y + 1]

    if below[x] == AIR:
        below[x] = row[x]
        row[x] = AIR
        return

    direction = -1 if random.getrandbits(1) else 1

    if direction == -1:

        if x > 0:
            if below[x - 1] == AIR or below[x - 1] == WATER:
                below[x - 1], row[x] = row[x], below[x - 1]
                return

        if x < MAP_W - 1:
            if below[x + 1] == AIR or below[x + 1] == WATER:
                below[x + 1], row[x] = row[x], below[x + 1]
                return

    else:

        if x < MAP_W - 1:
            if below[x + 1] == AIR or below[x + 1] == WATER:
                below[x + 1], row[x] = row[x], below[x + 1]
                return

        if x > 0:
            if below[x - 1] == AIR or below[x - 1] == WATER:
                below[x - 1], row[x] = row[x], below[x - 1]
                return

# ===== WATER =====

def update_water(world, x, y):

    row = world[y]
    below = world[y + 1]

    if below[x] == AIR:
        below[x] = WATER
        row[x] = AIR
        return

    direction = -1 if random.getrandbits(1) else 1

    # діагональ вниз
    if direction == -1:

        if x > 0 and below[x - 1] == AIR:
            below[x - 1] = WATER
            row[x] = AIR
            return

        if x < MAP_W - 1 and below[x + 1] == AIR:
            below[x + 1] = WATER
            row[x] = AIR
            return

    else:

        if x < MAP_W - 1 and below[x + 1] == AIR:
            below[x + 1] = WATER
            row[x] = AIR
            return

        if x > 0 and below[x - 1] == AIR:
            below[x - 1] = WATER
            row[x] = AIR
            return

    MAX_FLOW = 2

    for dx in (direction, -direction):

        for dist in range(1, MAX_FLOW + 1):

            nx = x + dx * dist

            if nx < 0 or nx >= MAP_W:
                break

            if row[nx] != AIR:
                break

            if below[nx] == AIR:
                row[nx] = WATER
                row[x] = AIR
                return

        nx = x + dx

        if 0 <= nx < MAP_W and row[nx] == AIR:
            row[nx] = WATER
            row[x] = AIR
            return

# ===== MAIN UPDATE =====

def update_materials(world):

    for y in range(MAP_H - 2, -1, -1):

        start = random.randint(0, MAP_W - 1)

        x = start

        for _ in range(MAP_W):

            tile = world[y][x]

            if tile == WATER:
                update_water(world, x, y)

            elif tile == SAND or tile == GRAVIY:
                update_sand(world, x, y)

            x += 1

            if x == MAP_W:
                x = 0