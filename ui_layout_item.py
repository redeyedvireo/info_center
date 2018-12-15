# ui_layout_item.py
#
# An element of a layout.

class UiLayoutItem:
    def __init__(self, layout, hAlignment):
        self.layout = layout
        self.hAlignment = hAlignment
        self.width = 0
        self.height = 0

    def computeRect(self, pygame):
        """ Determines the bounding rect of the item.  Subclasses will do this, based on their content. """
        pass

    def draw(self, screen, pos):
        """ Draws the item.   Subclasses know how to draw their content. """
        pass
