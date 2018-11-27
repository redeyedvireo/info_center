# screen.py
#
# The UiScreen class defines all the widgets for a complete screen.

import pygame
from button import Button
from touch_area import TouchArea
from button_strip import ButtonStrip
from ui_panel import UiPanel


class UiScreen:
    def __init__(self, pygame, screen):
        super(UiScreen, self).__init__()
        self.pygame = pygame
        self.screen = screen        # pygame screen

        self.buttonList = []
        self.touchAreaList = []
        self.buttonStripList = []
        self.panelList = []

    def display(self):
        """ Displays the screen.  This involves displaying all elements.
            This is typically done when a new screen comes into view. """
        for element in self.buttonList:
            element.draw(self.pygame, self.screen)

        for element in self.panelList:
            element.draw(self.pygame, self.screen)

        # Draw a frame around the touch areas, as required
        for touchArea in self.touchAreaList:
            touchArea.draw(self.pygame, self.screen)

    def addElement(self, uiElement):
        """ Registers the given UI element. """
        if isinstance(uiElement, Button):
            self.buttonList.append(uiElement)
        elif isinstance(uiElement, TouchArea):
            self.touchAreaList.append(uiElement)
        elif isinstance(uiElement, ButtonStrip):
            self.buttonStripList.append(uiElement)
            for button in uiElement.buttons:
                self.addElement(button)
        elif isinstance(uiElement, UiPanel):
            self.panelList.append(uiElement)

    def handleMouseButtonDown(self, event):
        self.pressUiElements(event.pos, self.buttonList)
        self.pressUiElements(event.pos, self.panelList)
        self.pressUiElements(event.pos, self.touchAreaList)
        return True

    def handleMouseButtonUp(self, event):
        self.unpressUiElements(event.pos, self.buttonList)
        self.unpressUiElements(event.pos, self.panelList)

        # For now, clicking a touch area will end the program
        if self.getHitUiElement(event.pos, self.touchAreaList) is not None:
            return False

        return True

    def pressUiElements(self, mousePos, uiElementList):
        uiElement = self.getHitUiElement(mousePos, uiElementList)
        if uiElement is not None:
            uiElement.setPressed()
            uiElement.draw(self.pygame, self.screen)

    def unpressUiElements(self, mousePos, uiElementList):
        uiElement = self.getHitUiElement(mousePos, uiElementList)
        if uiElement is not None:
            uiElement.setNormal()
            uiElement.draw(self.pygame, self.screen)

            if isinstance(uiElement, Button):
                uiElement.onClicked()

    def getHitUiElement(self, mousePos, uiElementList):
        for uiElement in uiElementList:
            if self.pointInElement(mousePos, uiElement):
                return uiElement

        return None

    def pointInElement(self, pos, uiElement):
        """ Determines if the given point is contained in the given element. """
        return uiElement.rect.collidepoint(pos)
