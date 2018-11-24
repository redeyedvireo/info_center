# button_strip.py
#
# A button strip holds a "strip" of buttons.  This is analogous to a linear layout
# in other frameworks.

# Properties:
#  - x
#  - y
#  - orientation (horiz or vert)
#  - position:
#      - cling to top
#      - cling to right side
#      - cling to bottom
#      - cling to left side
#      - absolute (in this mode, both x and y are specified by the user)
#        For the cling modes, either the x or y is implicit, depending on which
#        edge is being clung to.  For example, in "cling to right side", the
#        x is determined by the width of the largest button width.
class ButtonStrip:
    HORIZONTAL = 0
    VERTICAL = 1

    def __init__(self, x, y, orientation, spacing = 5):
        self.x = x
        self.y = y
        self.spacing = spacing
        self.orientation = orientation

        # This is where the next button will be inserted
        self.insertionPosX = x
        self.insertionPosY = y

        self.buttons = []

    def addButton(self, button):
        button.move(self.insertionPosX, self.insertionPosY)
        self.buttons.append(button)

        if self.orientation == self.HORIZONTAL:
            self.insertionPosX += button.rect.width + self.spacing
        else:
            self.insertionPosY += button.rect.height + self.spacing
