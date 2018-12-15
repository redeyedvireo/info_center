# ui_space_layout_item.py
#
# A layout item for empty space.

from ui_layout_item import UiLayoutItem
from ui_alignment import UiAlignment


class UiSpaceLayoutItem(UiLayoutItem):
    def __init__(self, layout, width, height):
        super(UiSpaceLayoutItem, self).__init__(layout, UiAlignment.LEFT)
        self.width = width
        self.height = height

    def computeRect(self, pygame):
        """ Nothing to do here! """
        pass

    def draw(self, screen, pos):
        """ Nothing to do here! """
        pass

