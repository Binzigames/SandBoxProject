# LOGIC ENGINE COUNTS MATH ETC
#importing for you honey ~
from SandEngine.Libs import *
from SandEngine.DATA.TMP import *
from SandEngine.Visuals.VisualEngine import *
from SandEngine.Debuger import *

Curent_material = 2
Fullscreen = False
def handle_controls():
    global Curent_material , Fullscreen
    mouse = pr.get_mouse_position()
    world_mouse = pr.get_screen_to_world_2d(mouse, camera)

    X = int(world_mouse.x // 4)
    Y = int(world_mouse.y // 4)
    radius = int(get_wheel_rotation())

    if pr.is_mouse_button_down(pr.MouseButton.MOUSE_BUTTON_LEFT):
        for x in range(-radius, radius + 1):
            for y in range(-radius, radius + 1):

                if x*x + y*y <= radius*radius:
                    world_set(X + x, Y + y, Curent_material)

        print_message(f"painted area at {X}, {Y} with scale {int(get_wheel_rotation())}" , 2)

    if pr.is_mouse_button_down(pr.MouseButton.MOUSE_BUTTON_RIGHT):


        for x in range(-radius, radius + 1):
            for y in range(-radius, radius + 1):

                if x*x + y*y <= radius*radius:
                    world_erase(X + x, Y + y)

    if pr.is_key_pressed(pr.KeyboardKey.KEY_ONE):
        Curent_material = 2
    if pr.is_key_pressed(pr.KeyboardKey.KEY_TWO):
        Curent_material = 3
    if pr.is_key_pressed(pr.KeyboardKey.KEY_THREE):
        Curent_material = 4
    if pr.is_key_pressed(pr.KeyboardKey.KEY_F11):
        Fullscreen = not Fullscreen

        if Fullscreen:
            pr.toggle_fullscreen()
        else:
            pr.toggle_fullscreen()
            pr.set_window_size(800, 900)


def handle_ui_buttons():
    global Curent_material
    button_width = 160
    button_height = 60
    spacing = 20
    panel_height = button_height + 40


    panel = pr.Rectangle(20,pr.get_screen_height() - panel_height - 10,pr.get_screen_width() - 40,panel_height)
    pr.draw_rectangle_rounded(pr.Rectangle( panel.x + 5,panel.y + 5,panel.width,panel.height),0.15,12,pr.Color(0, 0, 0, 100))
    pr.draw_rectangle_rounded( panel,0.15,12,pr.Color(25, 25, 35, 220))
    pr.draw_line(int(panel.x),int(panel.y),int(panel.x + panel.width),int(panel.y),pr.Color(80, 80, 100, 255),)


    y = pr.get_screen_height() - button_height - 20

    buttons = [
        (pr.Rectangle(50, y, button_width, button_height), "Sand", 2, pr.Color(220, 190, 90, 255)),
        (pr.Rectangle(50 + button_width + spacing, y, button_width, button_height), "Water", 3, pr.Color(70, 150, 240, 255)),
        (pr.Rectangle(50 + (button_width + spacing) * 2, y, button_width, button_height), "Wall", 4, pr.Color(120, 120, 120, 255)),
    ]

    mouse = pr.get_mouse_position()

    for rect, text, material, color in buttons:
        hovered = pr.check_collision_point_rec(mouse, rect)

        shadow = pr.Rectangle(rect.x + 5, rect.y + 5, rect.width, rect.height)
        pr.draw_rectangle_rounded(shadow, 0.2, 10, pr.Color(0, 0, 0, 80))


        if hovered:
            color = pr.Color(
                min(color.r + 30, 255),
                min(color.g + 30, 255),
                min(color.b + 30, 255),
                255
            )

        pr.draw_rectangle_rounded(rect, 0.2, 10, color)


        pr.draw_rectangle_rounded_lines(
            rect,
            0.2,
            10,
            pr.WHITE
        )


        text_width = pr.measure_text(text, 24)
        pr.draw_text(
            text,
            int(rect.x + rect.width / 2 - text_width / 2),
            int(rect.y + 18),
            24,
            pr.WHITE
        )

        if hovered and pr.is_mouse_button_pressed(pr.MouseButton.MOUSE_BUTTON_LEFT):
            Curent_material = material



    reset_rect = pr.Rectangle(
        pr.get_screen_width() - 220,
        y,
        200,
        60
    )

    hovered = pr.check_collision_point_rec(mouse, reset_rect)

    reset_color = pr.Color(200, 60, 60, 255)
    if hovered:
        reset_color = pr.Color(240, 80, 80, 255)

    pr.draw_rectangle_rounded(
        pr.Rectangle(reset_rect.x + 5, reset_rect.y + 5,
                     reset_rect.width, reset_rect.height),
        0.2,
        10,
        pr.Color(0,0,0,80)
    )

    pr.draw_rectangle_rounded(
        reset_rect,
        0.2,
        10,
        reset_color
    )

    pr.draw_rectangle_rounded_lines(
        reset_rect,
        0.2,
        10,
        pr.WHITE
    )

    text = "RESET"
    pr.draw_text(
        text,
        int(reset_rect.x + 55),
        int(reset_rect.y + 18),
        24,
        pr.WHITE
    )

    if hovered and pr.is_mouse_button_pressed(pr.MouseButton.MOUSE_BUTTON_LEFT):
        load_map()
