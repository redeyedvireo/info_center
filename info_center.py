#!/usr/bin/env python


# info_center.py
# A UI for viewing information about the environment.

import os, sys
import pygame
from pygame.locals import *
from ui_manager import UiManager
from ui_screen import UiScreen
from button import Button
from touch_area import TouchArea
from button_strip import ButtonStrip
from time_panel import TimePanel

WHITE = 255, 255, 255
#GRAY = 20, 20, 20
GRAY = 120, 120, 120
GREEN = 0, 255, 0
BLACK = 0, 0, 0
BLUE = 0, 0, 255
RED = 255, 0, 0

ONE_SECOND_EVENT = USEREVENT + 1

continueRunning = True


def backToMainScreen(uiManager):
    print("Yet another button clicked")
    uiManager.displayScreen("main")

def stopApp():
    global continueRunning
    continueRunning = False

def mainLoop():
    pygame.init()

    size = width, height = 800, 480
    # screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    screen = pygame.display.set_mode(size)
    pygame.time.set_timer(ONE_SECOND_EVENT, 1000)
    pygame.display.set_caption("Info Center")

    # JAG: Test fullscreen
    # pygame.display.toggle_fullscreen()

    # Now we draw onto a new surface, and blit the result to the screen

    # Create myimage and set transparency to top left pixel
    newsurface = pygame.Surface((80,80))
    myimage = newsurface.convert()
    ckey = myimage.get_at((0,0))
    myimage.set_colorkey(ckey, RLEACCEL)

    uiManager = UiManager(pygame, screen)

    # Create the main screen
    mainScreen = UiScreen(pygame, screen)

    # Create a button
    testButton = Button.createSolidButton(600, 200, 80, 80, (50, 100, 190), (200, 30, 140), lambda: uiManager.displayScreen("second"))
    mainScreen.addElement(testButton)

    # Create a Touch Area
    testTouchArea = TouchArea(0, 450, 800, 30, 1, lambda : stopApp())
    mainScreen.addElement(testTouchArea)

    # Create a Button Strip
    testButtonStrip = ButtonStrip(0, 350, ButtonStrip.HORIZONTAL, 25)
    button1 = Button.createSolidButton(0, 0, 40, 40, BLUE, (100, 150, 200), lambda: print("Button 1 clicked"))
    button2 = Button.createSolidButton(0, 0, 40, 40, BLUE, (150, 200, 100), lambda: print("Button 2 clicked"))
    button3 = Button.createSolidButton(0, 0, 40, 40, BLUE, (200, 100, 150), lambda: print("Button 3 clicked"))

    testButtonStrip.addButton(button1)
    testButtonStrip.addButton(button2)
    testButtonStrip.addButton(button3)

    # Create a vertical Button Strip
    testVerticalButtonStrip = ButtonStrip(759, 0, ButtonStrip.VERTICAL)
    button4 = Button.createSolidButton(0, 0, 40, 40, BLUE, (100, 150, 200), lambda: print("Button 4 clicked"))
    button5 = Button.createSolidButton(0, 0, 40, 40, BLUE, (150, 200, 100), lambda: print("Button 5 clicked"))
    button6 = Button.createSolidButton(0, 0, 40, 40, BLUE, (200, 100, 150), lambda: print("Button 6 clicked"))

    testVerticalButtonStrip.addButton(button4)
    testVerticalButtonStrip.addButton(button5)
    testVerticalButtonStrip.addButton(button6)

    mainScreen.addElement(testButtonStrip)
    mainScreen.addElement(testVerticalButtonStrip)

    # Create a TimePanel
    #timePanel = TimePanel(0, 0, 410, 150, 1, GREEN, BLUE)
    timePanel = TimePanel(0, 0, 630, 150, 1, GREEN, BLUE)       # This width is temporary

    mainScreen.addElement(timePanel)

    uiManager.addScreen("main", mainScreen)

    # Create a second screen
    secondScreen = UiScreen(pygame, screen)
    secondScreenButton = Button.createSolidButton(400, 240, 100, 100, BLUE, GREEN, lambda : backToMainScreen(uiManager))
    secondScreen.addElement(secondScreenButton)
    uiManager.addScreen("second", secondScreen)

    uiManager.displayScreen("main")

    while continueRunning:
        for event in pygame.event.get():
            if event.type == ONE_SECOND_EVENT:
                uiManager.updateUiElements()

            if uiManager.handleEvents(event):
                pygame.display.update()

                # TODO: Determine if a delay is necessary here.  Does lack of a delay cause a CPU spike?
                pygame.time.delay(200)
            else:
                pygame.display.quit()
                sys.exit(0)

    # while 1:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.display.quit()
    #             sys.exit(0)
    #         elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
    #             pygame.display.quit()
    #             sys.exit(0)
    #         elif event.type == pygame.MOUSEBUTTONUP:
    #             pygame.display.quit()
    #             sys.exit(0)
    #         else:
    #             pygame.display.update()
    #             pygame.time.delay(500)


# ---------------------------------------------------------------
if __name__ == "__main__":
    mainLoop()
