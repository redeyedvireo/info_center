# time_panel.py
#
# A panel that displays the current time.

import datetime
from ui_panel import UiPanel
from ui_colors import UiColors


class TimePanel(UiPanel):
    def __init__(self, x, y, width, height, borderWidth, unpressedBackground, pressedBackground):
        super(TimePanel, self).__init__(x, y, width, height, True, borderWidth, unpressedBackground, pressedBackground)
        self.currentHoursMinutesStr, self.currentSecondsStr = self.timeString()
        self.previousHoursMinutesStr = ""
        self.previousSecondsStr = ""

    def draw(self, pygame, screen):
        super(TimePanel, self).draw(pygame, screen)
        font = pygame.font.Font(None, 220)
        fontimg = font.render(self.currentHoursMinutesStr, 1, UiColors.GRAY)
        screen.blit(fontimg, self.pos())
        smallerFont = pygame.font.Font(None, 100)
        secondsImage = smallerFont.render(self.currentSecondsStr, 1, UiColors.GRAY)
        curPosX, curPosY = self.pos()
        #newPos = curPosX + 400, curPosY + 10       # Hang the seconds at the top
        # newPos = curPosX + 400, curPosY + 68        # Drop the seconds at the bottom
        newPos = curPosX + fontimg.get_width() + 4, curPosY + 68 
        screen.blit(secondsImage, newPos)

    def timeString(self):
        """ Returns the time as a tuple of the form:
            (HH:MM, SS). """
        curTime = datetime.datetime.now()
        return curTime.strftime('%H:%M'), curTime.strftime('%S')

    def setNormal(self):
        super(TimePanel, self).setNormal()

    def setPressed(self):
        super(TimePanel, self).setPressed()

    def update(self, pygame, screen):
        """ Updates the time.  Redraws, as necessary. """
        tempHoursMinutesStr, tempSecondsStr = self.timeString()

        if tempSecondsStr != self.currentSecondsStr:
            self.previousHoursMinutesStr = self.currentSecondsStr
            self.previousSecondsStr = tempSecondsStr
            self.currentHoursMinutesStr = tempHoursMinutesStr
            self.currentSecondsStr = tempSecondsStr
            self.draw(pygame, screen)
