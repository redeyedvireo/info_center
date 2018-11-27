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

    def draw(self, pygame, screen):
        super(TimePanel, self).draw(pygame, screen)
        font = pygame.font.Font(None, 220)
        timeStr = self.timeString()
        fontimg = font.render(timeStr, 1, GRAY)
        screen.blit(fontimg, self.pos())

    def timeString(self):
        return datetime.datetime.now().strftime('%H:%M')

    def setNormal(self):
        super(TimePanel, self).setNormal()

    def setPressed(self):
        super(TimePanel, self).setPressed()
