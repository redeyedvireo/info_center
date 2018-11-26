# ui_manager.py
#
# Manages all UI elements.
# Keeps track of all UI elements.  Every UI element must be registered
# with the UiManager.  UI elements have callback functions that are
# called when the user interacts with them.

import pygame
from button import Button
from touch_area import TouchArea
from button_strip import ButtonStrip


class UiManager:
    def __init__(self, pygame, screen):
        super(UiManager, self).__init__()
        self.pygame = pygame
        self.screen = screen

        # A map of screen IDs to UiScreen objects.
        self.screenMap = {}

        self.currentScreen = None

    def addScreen(self, id, uiScreen):
        self.screenMap[id] = uiScreen

    def displayScreen(self, id):
        self.currentScreen = self.screenMap[id]
        self.screen.fill((0, 0, 0))
        self.currentScreen.display()


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
