input.onButtonPressed(Button.A, function on_button_pressed_a() {
    sprite.change(LedSpriteProperty.X, -1)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    sprite.change(LedSpriteProperty.X, 1)
})
let sprite : game.LedSprite = null
music.setBuiltInSpeakerEnabled(true)
sprite = game.createSprite(0, 2)
let win = game.createSprite(4, 2)
basic.forever(function on_forever() {
    music.playMelody("A G A G F G A B ", 120)
})
basic.forever(function on_forever2() {
    if (sprite.isTouching(win)) {
        win.delete()
        sprite.delete()
        basic.clearScreen()
        basic.showIcon(IconNames.Heart)
        basic.pause(2000)
        basic.showString("yay you win")
    }
    
})
