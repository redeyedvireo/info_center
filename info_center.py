#!/usr/bin/env python


# info_center.py
# A UI for viewing information about the environment.

import os, sys
import pygame
from pygame.locals import *
from ui_manager import UiManager
from button import Button
from touch_area import TouchArea

WHITE = 255, 255, 255
#GRAY = 20, 20, 20
GRAY = 120, 120, 120
GREEN = 0, 255, 0
BLACK = 0, 0, 0
BLUE = 0, 0, 255
RED = 255, 0, 0


pygame.init()

size = width, height = 800, 480
# screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Info Center")

# JAG: Test fullscreen
# pygame.display.toggle_fullscreen()

# Now we draw onto a new surface, and blit the result to the screen

# Create myimage and set transparency to top left pixel
newsurface = pygame.Surface((80,80))
myimage = newsurface.convert()
ckey = myimage.get_at((0,0))
myimage.set_colorkey(ckey, RLEACCEL)


# Show the time
font = pygame.font.Font(None, 220)
fontimg1 = font.render("12:34", 1, GRAY)
screen.blit(fontimg1, (0,0))

uiManager = UiManager(pygame, screen)

# Create a button
testButton = Button.createSolidButton(600, 100, 80, 80, (50, 100, 190), (200, 30, 140))
uiManager.addElement(testButton)

# Create a Touch Area
testTouchArea = TouchArea(0, 450, 800, 30, 1)
uiManager.addElement(testTouchArea)

uiManager.performInitialDraw()

while 1:
    for event in pygame.event.get():
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
