def on_button_pressed_a():
    sprite.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    sprite.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

sprite: game.LedSprite = None
music.set_built_in_speaker_enabled(True)
sprite = game.create_sprite(0, 2)
win = game.create_sprite(4, 2)

def on_forever():
    music.play_melody("A G A G F G A B ", 120)
basic.forever(on_forever)

def on_forever2():
    if sprite.is_touching(win):
        win.delete()
        sprite.delete()
        basic.clear_screen()
        basic.show_icon(IconNames.HEART)
        basic.pause(2000)
        basic.show_string("yay you win")
basic.forever(on_forever2)
