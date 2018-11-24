# touch_area.py
#
# Touch area class.  Provides an area that the user can click on, without
# any displayable content.

class TouchArea(ScreenElement):
    # Properties
    #  - x
    #  - y
    #  - onClicked - when button is clicked (pressed, then unpressed)
    #  - onPressed - when button pressed (ie, pushed in)
    #  - onReleased - when button released
