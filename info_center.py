#!/usr/bin/env python


# info_center.py
# A UI for viewing information about the environment.

from optparse import OptionParser
import subprocess
import pygame
import configparser
from pygame.locals import *
from ui_manager import UiManager
from button import Button
from touch_area import TouchArea
from button_strip import ButtonStrip
from time_panel import TimePanel
from weather_panel import WeatherPanel

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


def turnOffBacklight():
    print("Attempting to turn off backlight")
    command1 = "echo 1"
    command2 = "/usr/bin/sudo /usr/bin/tee /sys/class/backlight/rpi_backlight/bl_power"
    process1 = subprocess.Popen(command1.split(), stdout=subprocess.PIPE)
    process2 = subprocess.Popen(command2.split(), stdin=process1.stdout, stdout=subprocess.PIPE)
    output = process2.communicate()[0]
    print(output)

def readConfig():
    """ Reads the config file.  For now, only the weather config is returned. """
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    return (config['weather']['zipcode'], config['weather']['appid'])

def mainLoop(windowedMode):
    pygame.init()

    zipcode, weatherAppId = readConfig()

    size = width, height = 800, 480
    if windowedMode:
        screen = pygame.display.set_mode(size)
    else:
        screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

    pygame.display.set_caption("Info Center")

    # Create myimage and set transparency to top left pixel
    newsurface = pygame.Surface((80,80))
    myimage = newsurface.convert()
    ckey = myimage.get_at((0,0))
    myimage.set_colorkey(ckey, RLEACCEL)

    uiManager = UiManager(pygame, screen)

    # Create the main screen
    mainScreen = uiManager.addScreen("main")

    # Create a button
    testButton = Button.createSolidButton(719, 0, 80, 80, (50, 100, 190), (200, 30, 140), lambda: uiManager.displayScreen("second"))
    mainScreen.addElement(testButton)

    # Create a Touch Area
    testTouchArea = TouchArea(0, 450, 800, 30, 1, lambda : uiManager.terminate())
    mainScreen.addElement(testTouchArea)

    # Create a TimePanel
    timePanel = TimePanel(0, 0, 500, 150, 1, BLACK, BLUE)

    # Create a WeatherPanel
    # TODO: Ideally, the WeatherPanel should set its own size
    weatherPanel = WeatherPanel(0, 170, 300, 250, 2, BLACK, BLUE, appid=weatherAppId, zipcode=zipcode)

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
    screenOffButton = Button.createSolidButton(759, 399, 40, 40, GREEN, BLUE, lambda: turnOffBacklight())
    secondScreen.addElement(screenOffButton)

    uiManager.displayScreen("main")

    # Add some timers
    # uiManager.setTimer(seconds=2, callback=lambda: print("2-second timer triggered."))
    # uiManager.setTimer(seconds=5, callback=lambda: print("5-second timer triggered."))
    # uiManager.setTimer(seconds=9, callback=lambda: print("9-second timer triggered."))
    # uiManager.setTimer(minutes=1, callback=lambda: print("1-minute timer triggered."))

    uiManager.run()


# ---------------------------------------------------------------
if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-w", "--windowed", action="store_true", default=False, dest="windowed", help="Use windowed mode instead of full-screen")

    (options, args) = parser.parse_args()
    mainLoop(options.windowed)
