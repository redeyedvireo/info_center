# touch_area.py
#
# Touch area class.  Provides an area that the user can click on, without
# any displayable content.

from ui_element import UiElement


class TouchArea(UiElement):
    # Properties
    #  - x
    #  - y
    #  - borderWidth - Thickness of border drawn around the area (Set to 0 for no border)
    #  - onClicked - when button is clicked (pressed, then unpressed)
    #  - onPressed - when button pressed (ie, pushed in)
    #  - onReleased - when button released
    def __init__(self, x, y, width, height, borderWidth):
        super(TouchArea, self).__init__(x, y, width, height, borderWidth)
