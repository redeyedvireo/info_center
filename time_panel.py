# time_panel.py
#
# A panel that displays the current time.

import datetime
from ui_panel import UiPanel
from ui_utility import UiUtility
from ui_alignment import UiAlignment

class TimePanel(UiPanel):
    def __init__(self, x, y, width, height, borderWidth, unpressedBackground, pressedBackground):
        super(TimePanel, self).__init__(x, y, width, height, True, borderWidth, unpressedBackground, pressedBackground)
        self.currentHoursMinutesStr, self.currentSecondsStr, self.amPmStr, self.dateStr = self.timeString()
        self.previousHoursMinutesStr = ""
        self.previousSecondsStr = ""

    def draw(self, pygame, screen):
        super(TimePanel, self).draw(pygame, screen)

        timeImage = UiUtility.drawText(pygame, screen, self.pos(), self.currentHoursMinutesStr, 220)

        curPosX, curPosY = self.pos()
        secondsPos = curPosX + timeImage.get_width() + 4, curPosY + 68
        secondsImage = UiUtility.drawText(pygame, screen, secondsPos, self.currentSecondsStr, 100)

        amPmPos = secondsPos[0], curPosY + 10       # Hang AM/PM at the top
        amRect = pygame.Rect(secondsPos[0], curPosY, secondsImage.get_width(), secondsImage.get_height())
        UiUtility.drawText(pygame, screen, amPmPos, self.amPmStr, 50, hAlign=UiAlignment.HCENTER, vAlign=UiAlignment.BOTTOM, box=amRect)

        datePos = curPosX, curPosY + timeImage.get_height()
        UiUtility.drawText(pygame, screen, datePos, self.dateStr, 30, hAlign=UiAlignment.HCENTER, vAlign=UiAlignment.BOTTOM, box=self.rect)

    def timeString(self):
        """ Returns the time as a tuple of the form:
            (HH:MM, SS, AM|PM, date). """
        curTime = datetime.datetime.now()
        return curTime.strftime('%I:%M'), curTime.strftime('%S'), curTime.strftime('%p'), curTime.strftime('%A, %B %d, %Y')

    def setNormal(self):
        super(TimePanel, self).setNormal()

    def setPressed(self):
        super(TimePanel, self).setPressed()

    def update(self, pygame, screen):
        """ Updates the time.  Redraws, as necessary. """
        tempHoursMinutesStr, tempSecondsStr, amPmStr, dateStr = self.timeString()

        if tempSecondsStr != self.currentSecondsStr:
            self.previousHoursMinutesStr = self.currentSecondsStr
            self.previousSecondsStr = tempSecondsStr
            self.currentHoursMinutesStr = tempHoursMinutesStr
            self.currentSecondsStr = tempSecondsStr
            self.dateStr = dateStr
            self.amPmStr = amPmStr
            self.draw(pygame, screen)
