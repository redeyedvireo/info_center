# button.py
#
# Button class.

class Button(ScreenElement):
    # Properties
    #  - unpressed image
    #  - pressed image
    #  - x
    #  - y
    #  - onClicked - when button is clicked (pressed, then unpressed)
    #  - onPressed - when button pressed (ie, pushed in)
    #  - onReleased - when button released
    def __init__(self, x, y, width, height, normalImage, pressedImage):
        super(x, y, width, height)
        self.normalImage = normalImage
        self.pressedImage = pressedImage
