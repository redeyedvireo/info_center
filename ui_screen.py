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
        self.pressButton(event.pos)
        return True

    def handleMouseButtonUp(self, event):
        self.unpressButton(event.pos)
        if self.touchAreaHitTest(event.pos):
            return False
        return True

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
        for button in self.buttonList:
            if self.pointInElement(mousePos, button):
                return button

        return None

    def getHitTouchArea(self, mousePos):
        for touchArea in self.touchAreaList:
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
