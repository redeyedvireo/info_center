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
        #self.pygame.fill.rect(self.screen, (0, 0, 0), (0, 0, 800, 480))
        self.screen.fill((0, 0, 0))
        self.currentScreen.display()

    def pressButton(self, mousePos):
        button = self.getHitButton(mousePos)
        if button is not None:
            button.setPressed()
            button.draw(self.pygame, self.screen)

    def unpressButton(self, mousePos):
        button = self.getHitButton(mousePos)
        if button is not None:
            button.setNormal()
            button.draw(self.pygame, self.screen)
            button.onClicked()

    def getHitButton(self, mousePos):
        for button in self.currentScreen.buttonList:
            if self.pointInElement(mousePos, button):
                return button

        return None

    def getHitTouchArea(self, mousePos):
        for touchArea in self.currentScreen.touchAreaList:
            if self.pointInElement(mousePos, touchArea):
                return touchArea

        return None

    def touchAreaHitTest(self, mousePos):
        touchArea = self.getHitTouchArea(mousePos)
        if touchArea is not None:
            return True
        else:
            return False

    def pointInElement(self, pos, uiElement):
        """ Determines if the given point is contained in the given element. """
        return uiElement.rect.collidepoint(pos)

    # This should probably return a code that indicates whether the app
    # should change its status, such as to quit, or blank the screen, etc.
    # Returns True if the app should continue, False if the app should quit.
    def handleEvents(self, event):
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.pressButton(event.pos)
            return True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.unpressButton(event.pos)
            if self.touchAreaHitTest(event.pos):
                return False
            return True
        else:
            return True
