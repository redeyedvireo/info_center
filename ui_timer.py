# ui_timer.py
#
# A user-settable timer.


class UiTimer:
    def __init__(self, timerInterval, callback):
        """ The timer interval is in seconds. """
        super(UiTimer, self).__init__()
        self.interval = timerInterval
        self.callback = callback

        # Keeps track of the current value.  It counts down every tick, and when it reaches 0,
        # the callback function is called.
        self.currentValue = timerInterval

    def tick(self):
        """ Initiates a timer tick.  This should be called by the framework every second.
            When the timer is triggered, the callback function is called. """
        self.currentValue -= 1

        if self.currentValue == 0:
            self.callback()
            self.currentValue = self.interval
