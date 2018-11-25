# ui_panel.py
#
# Class for UiPanel.  This will have various properties and behaviors that are
# common to all panels.  A panel generally draws its own content.

from ui_element import UiElement


class UiPanel(UiElement):
    def __init__(self, x, y, width, height, clickable, pygame, screen):
        super(UiPanel, self).__init__(x, y, width, height)
        self.clickable = clickable
        self.pygame = pygame
        self.screen = screen

    def draw(self):
        pass

# TODO: Some behaviors this class should have:
#       - clickability.  When clicked, it will either change the background color, or show an outline around the panel