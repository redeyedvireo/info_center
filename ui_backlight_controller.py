# ui_backlight_controller.py
#
# Manages the backlight of the touchscreen.

import subprocess


class UiBacklightController:
    ON = 1
    OFF = 0
    BACKLIGHT_TIMER_ID = "backlight_timer"

    def __init__(self):
        self.uiManager = None
        self.currentState = self.ON
        self.disabled = False

    def init(self, uiManager):
        self.uiManager = uiManager

        # Set a timer to turn off the backlight after a period of time.
        # TODO: Will need to reset the timer whenever there is user activity
        #self.uiManager.setTimer(timerId=self.BACKLIGHT_TIMER_ID, minutes=3, callback=self.turnOffBacklight)
        self.uiManager.setTimer(timerId=self.BACKLIGHT_TIMER_ID, seconds=30, callback=self.turnOffBacklight)     # For debugging

    def resetUiTimeout(self):
        timer = self.uiManager.getTimer(self.BACKLIGHT_TIMER_ID)
        timer.reset()

    def isOn(self):
        return self.currentState == self.ON

    def turnOffBacklight(self):
        if not self.disabled:
            print("Attempting to turn off backlight")
            command1 = "echo 1"
            command2 = "/usr/bin/sudo /usr/bin/tee /sys/class/backlight/rpi_backlight/bl_power"
            process1 = subprocess.Popen(command1.split(), stdout=subprocess.PIPE)
            process2 = subprocess.Popen(command2.split(), stdin=process1.stdout, stdout=subprocess.PIPE)
            output = process2.communicate()[0]
            print(output)
        else:
            print("Backlight is OFF")
            self.currentState = self.OFF

    def turnOnBacklight(self):
        if not self.disabled:
            print("Attempting to turn on backlight")
            command1 = "echo 0"
            command2 = "/usr/bin/sudo /usr/bin/tee /sys/class/backlight/rpi_backlight/bl_power"
            process1 = subprocess.Popen(command1.split(), stdout=subprocess.PIPE)
            process2 = subprocess.Popen(command2.split(), stdin=process1.stdout, stdout=subprocess.PIPE)
            output = process2.communicate()[0]
            print(output)
        else:
            print("Backlight is ON")
            self.currentState = self.ON

    def syncBacklightState(self):
        with open("/sys/class/backlight/rpi_backlight/bl_power", "r") as f:
            val = int(f.read())
            self.currentState = self.ON if val == 0 else self.OFF

