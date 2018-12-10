# ui_manager.py
#
# Manages all UI elements.
# Keeps track of all UI elements.  Every UI element must be registered
# with the UiManager.  UI elements have callback functions that are
# called when the user interacts with them.

import pygame
from ui_timer import UiTimer


class UiManager:
    def __init__(self, pygame, screen):
        super(UiManager, self).__init__()
        self.ONE_SECOND_EVENT = pygame.USEREVENT + 1

        self.pygame = pygame
        self.screen = screen

        # A map of screen IDs to UiScreen objects.
        self.screenMap = {}

        # User timers.
        self.timers = []

        self.currentScreen = None
        self.continueRunning = True

    def addScreen(self, id, uiScreen):
        self.screenMap[id] = uiScreen

    def displayScreen(self, id):
        self.currentScreen = self.screenMap[id]
        self.screen.fill((0, 0, 0))
        self.currentScreen.display()

    def setTimer(self, seconds=None, minutes=None, hours=None, callback=None):
        """ Sets a timer, that triggers for the given time interval.  The time inverval is specified as
            follows:
                - if seconds are specified, that is used for the interval.
                - next, minutes are checked, and if specified, minutes are used to specify the interval.
                - finally, hours are checked, and if specified, hours are used to specify the interval.
                - callback specifies a function to call when the timer is triggered. """
        timerInterval = 0       # Seconds
        if seconds is not None:
            timerInterval = seconds
        elif minutes is not None:
            timerInterval = minutes * 60
        elif hours is not None:
            timerInterval = hours * 3600

        if timerInterval > 0 and callback is not None:
            self.timers.append( UiTimer(timerInterval, callback) )

    # This should probably return a code that indicates whether the app
    # should change its status, such as to quit, or blank the screen, etc.
    # Returns True if the app should continue, False if the app should quit.
    def handleEvents(self, event):
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            return self.currentScreen.handleMouseButtonDown(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            return self.currentScreen.handleMouseButtonUp(event)
        else:
            return True

    def updateUiElements(self):
        self.currentScreen.updateUiElements()

    def updateTimers(self):
        for timer in self.timers:
            timer.tick()

    def terminate(self):
        """ Stops the event loop. """
        self.continueRunning = False

    def run(self):
        """ Runs the event loop. """

        # Set internal timers
        pygame.time.set_timer(self.ONE_SECOND_EVENT, 1000)

        while self.continueRunning:
            for event in pygame.event.get():
                if event.type == self.ONE_SECOND_EVENT:
                    self.updateUiElements()
                    self.updateTimers()

                if self.handleEvents(event):
                    pygame.display.update()

                    # TODO: Determine if a delay is necessary here.  Does lack of a delay cause a CPU spike?
                    pygame.time.delay(200)
                else:
                    pygame.display.quit()
                    return
