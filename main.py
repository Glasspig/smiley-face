basic.show_icon(IconNames.SAD)
def on_button_pressed_a():
    basic.show_icon(IconNames.HAPPY)
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)
def on_button_pressed_b():
    basic.show_icon(IconNames.SAD)
    pass
input.on_button_pressed(Button.B, on_button_pressed_b)