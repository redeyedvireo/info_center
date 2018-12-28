#!/usr/bin/env python


# info_center.py
# A UI for viewing information about the environment.

import os
import argparse
import pygame
import configparser
from pygame.locals import *
from ui_manager import UiManager
from ui_backlight_controller import UiBacklightController
from button import Button
from touch_area import TouchArea
from button_strip import ButtonStrip
from time_panel import TimePanel
from weather_panel import WeatherPanel

scriptDir = os.path.dirname(os.path.realpath(__file__))

WHITE = 255, 255, 255
GRAY = 20, 20, 20
#GRAY = 120, 120, 120
GREEN = 0, 255, 0
BLACK = 0, 0, 0
BLUE = 0, 0, 255
RED = 255, 0, 0

CONFIG_FILE = 'info_center.ini'


def backToMainScreen(uiManager):
    print("Yet another button clicked")
    uiManager.displayScreen("main")

def readConfig():
    """ Reads the config file.  For now, only the weather config is returned. """
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    return (config['weather']['zipcode'], config['weather']['appid'])

def mainLoop(windowedMode, noBacklight):
    pygame.init()

    zipcode, weatherAppId = readConfig()

    size = width, height = 800, 480
    if windowedMode:
        screen = pygame.display.set_mode(size)
    else:
        screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

    pygame.display.set_caption("Info Center")

    backlightController = UiBacklightController()

    backlightController.disabled = noBacklight

    uiManager = UiManager(pygame, screen, backlightController)
    uiManager.init()

    # Create the main screen
    mainScreen = uiManager.addScreen("main")

    # Create a button
    testButton = Button.createSolidButton(719, 399, 80, 80, (50, 100, 190), (200, 30, 140), lambda: uiManager.displayScreen("second"))
    mainScreen.addElement(testButton)

    # Create a Touch Area
    # testTouchArea = TouchArea(0, 450, 800, 30, 1, lambda : uiManager.terminate())
    # mainScreen.addElement(testTouchArea)

    # Exit button

    # exitPressedSurface = pygame.Surface((exitImage.get_width(), exitImage.get_height()))
    # exitPressedSurface.fill(WHITE)
    # exitPressedSurface.blit(exitImage, (0, 0), special_flags=BLEND_RGBA_ADD)

    # exitButton = Button.createSolidButton(0, 399, 80, 80, RED, BLUE, lambda: uiManager.terminate())

    exitButton = Button.createButton(0, 432, "exit.png", "exit-pressed.png", lambda : uiManager.terminate())
    mainScreen.addElement(exitButton)

    # Create a TimePanel
    timePanel = TimePanel(0, 0, 500, 150, 1, BLACK, BLUE)

    # Create a WeatherPanel
    # TODO: Ideally, the WeatherPanel should set its own size
    weatherPanel = WeatherPanel(500, 0, 300, 250, 0, BLACK, BLUE, appid=weatherAppId, zipcode=zipcode)

    mainScreen.addElement(timePanel)
    mainScreen.addElement(weatherPanel)

    # Create a second screen
    secondScreen = uiManager.addScreen("second")

    secondScreenButton = Button.createSolidButton(599, 0, 100, 100, BLUE, GREEN, lambda : backToMainScreen(uiManager))
    secondScreen.addElement(secondScreenButton)

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

    secondScreen.addElement(testButtonStrip)
    secondScreen.addElement(testVerticalButtonStrip)

    # Add "Screen Off" button
    screenOffButton = Button.createSolidButton(759, 399, 40, 40, GREEN, BLUE, lambda: uiManager.turnOffBacklight())
    secondScreen.addElement(screenOffButton)
    
    # Add "Screen On" button
    screenOnButton = Button.createSolidButton(715, 399, 40, 40, BLUE, GREEN, lambda: uiManager.turnOnBacklight())
    secondScreen.addElement(screenOnButton)

    uiManager.displayScreen("main")

    # Add some timers
    # uiManager.setTimer(seconds=2, callback=lambda: print("2-second timer triggered."))
    # uiManager.setTimer(seconds=5, callback=lambda: print("5-second timer triggered."))
    # uiManager.setTimer(seconds=9, callback=lambda: print("9-second timer triggered."))
    # uiManager.setTimer(minutes=1, callback=lambda: print("1-minute timer triggered."))

    uiManager.run()


# ---------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--windowed", action="store_true", default=False, dest="windowed", help="Use windowed mode instead of full-screen")
    parser.add_argument("--no_backlight", action="store_true", default=False, dest="no_backlight", help="Disable backlight control")

    args = parser.parse_args()
    mainLoop(args.windowed, args.no_backlight)
