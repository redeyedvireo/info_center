# ui_panel.py
#
# Class for UiPanel.  This will have various properties and behaviors that are
# common to all panels.  A panel generally draws its own content.

from ui_element import UiElement


class UiPanel(UiElement):
    def __init__(self, x, y, width, height, clickable, borderWidth):
        super(UiPanel, self).__init__(x, y, width, height, borderWidth)
        self.clickable = clickable

    def draw(self, pygame, screen):
        super(UiPanel, self).draw(pygame, screen)

# TODO: Some behaviors this class should have:
#       - clickability.  When clicked, it will either change the background color, or show an outline around the panel