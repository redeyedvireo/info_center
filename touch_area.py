# touch_area.py
#
# Touch area class.  Provides an area that the user can click on, without
# any displayable content.

from ui_element import UiElement


class TouchArea(UiElement):
    # Properties
    #  - x
    #  - y
    #  - onClicked - when button is clicked (pressed, then unpressed)
    #  - onPressed - when button pressed (ie, pushed in)
    #  - onReleased - when button released
    def __init__(self, x, y, width, height):
        super(TouchArea, self).__init__(x, y, width, height)
