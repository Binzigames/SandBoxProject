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

    y = pr.get_screen_height() - button_height - 20

    buttons = [
        (pr.Rectangle(50, y, button_width, button_height), "Sand", 2),
        (pr.Rectangle(50 + button_width + spacing, y, button_width, button_height), "Water", 3),
        (pr.Rectangle(50 + (button_width + spacing) * 2, y, button_width, button_height), "Wall", 4),
    ]

    for rect, text, material in buttons:
        if pr.gui_button(rect, text):
            Curent_material = material