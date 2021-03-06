# ui_screensaver.py
#
# Manages screensavers.

from ui_screen import UiScreen


class UiScreenSaver(UiScreen):
    SCREEN_SAVER_TIMER_ID = "screen_saver_timer"
    SCREEN_ID = "screen_saver"

    def __init__(self, pygame, screen):
        super(UiScreenSaver, self).__init__(None, pygame, screen)

        self.currentScreenId = ""
        self.active = False

    def init(self, uiManager):
        self.uiManager = uiManager

        self.uiManager.setTimer(timerId=self.SCREEN_SAVER_TIMER_ID, minutes=5, callback=self.screenSaverTrigger)
        #self.uiManager.setTimer(timerId=self.SCREEN_SAVER_TIMER_ID, seconds=10, callback=self.screenSaverTrigger)  # DEBUG

    def screenSaverTrigger(self):
        print("Screen Saver triggered.")
        if not self.active:
            self.active = True
            self.currentScreenId = self.uiManager.currentScreenId
            self.uiManager.displayScreen(self.SCREEN_ID)
            self.uiManager.turnOffBacklight()

    def resetUiTimeout(self):
        timer = self.uiManager.getTimer(self.SCREEN_SAVER_TIMER_ID)
        timer.reset()

    def handleMouseButtonUp(self, event):
        # Any touch event will end the screen saver.
        self.active = False
        self.uiManager.displayScreen(self.currentScreenId)
        self.uiManager.updateUiElements()
        self.uiManager.turnOnBacklight()
        self.resetUiTimeout()
        return True
