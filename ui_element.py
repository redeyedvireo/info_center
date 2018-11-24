# ui_element.py
#
# UiElement is the base class for all UI controls.

class UiElement:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def size(self):
        return (width, height)
    
    def pos(self):
        return (x, y)
