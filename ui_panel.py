# ui_panel.py
#
# Class for UiPanel.  This will have various properties and behaviors that are
# common to all panels.  A panel generally draws its own content.

from ui_element import UiElement


class UiPanel(UiElement):
    # Button states
    STATE_UNPRESSED = 0
    STATE_PRESSED = 1

    def __init__(self, x, y, width, height, clickable, borderWidth, unpressedBackground, pressedBackground, onClickedFunc):
        super(UiPanel, self).__init__(x, y, width, height, borderWidth)
        self.clickable = clickable
        self.unpressedBackground = unpressedBackground
        self.pressedBackground = pressedBackground
        self.state = self.STATE_UNPRESSED
        self.onClickedFunc = onClickedFunc

    def init(self, uiManager):
        """ Callback where initialization can happen.  This would include more time-consuming tasks such
            as fetching data from the network, or loading files from disk.  Subclasses will override this
            as needed. """
        pass

    def draw(self, pygame, screen):
        super(UiPanel, self).draw(pygame, screen)

        # Draw background
        if self.state == self.STATE_UNPRESSED:
            pygame.draw.rect(screen, self.unpressedBackground, self.rect, 0)
        else:
            pygame.draw.rect(screen, self.pressedBackground, self.rect, 0)

    def setNormal(self):
        self.state = self.STATE_UNPRESSED

    def setPressed(self):
        self.state = self.STATE_PRESSED

    def onClicked(self):
        if self.onClickedFunc is not None:
            self.onClickedFunc()

# TODO: Some behaviors this class should have:
#       - clickability.  When clicked, it will either change the background color, or show an outline around the panel