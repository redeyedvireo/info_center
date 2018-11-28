# time_panel.py
#
# A panel that displays the current time.

import datetime
from ui_panel import UiPanel

# GRAY = 20, 20, 20
GRAY = 120, 120, 120


class TimePanel(UiPanel):
    def __init__(self, x, y, width, height, borderWidth, unpressedBackground, pressedBackground):
        super(TimePanel, self).__init__(x, y, width, height, True, borderWidth, unpressedBackground, pressedBackground)
        self.currentTimeStr = self.timeString()
        self.previousTimeStr = ""

    def draw(self, pygame, screen):
        super(TimePanel, self).draw(pygame, screen)
        font = pygame.font.Font(None, 220)
        fontimg = font.render(self.currentTimeStr, 1, GRAY)
        screen.blit(fontimg, self.pos())

    def timeString(self):
        return datetime.datetime.now().strftime('%H:%M:%S')

    def setNormal(self):
        super(TimePanel, self).setNormal()

    def setPressed(self):
        super(TimePanel, self).setPressed()

    def update(self, pygame, screen):
        """ Updates the time.  Redraws, as necessary. """
        tempTimeStr = self.timeString()

        if tempTimeStr != self.currentTimeStr:
            self.previousTimeStr = self.currentTimeStr
            self.currentTimeStr = tempTimeStr
            self.draw(pygame, screen)
