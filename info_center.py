#!/usr/bin/env python


# info_center.py
# A UI for viewing information about the environment.

import os, sys, pygame
from pygame.locals import *
from math import pi

WHITE = 255,255,255
GRAY = 20,20,20
GREEN = 0,255,0
BLACK = 0,0,0
BLUE  = 0,0,255
RED   = 255,0,0


size = width, height = 800, 480
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
pygame.display.set_caption("Info Center")
pygame.init()

# JAG: Test fullscreen
#pygame.display.toggle_fullscreen()

#now we draw onto a new surface, and blit the result to the screen

#create myimage and set transparancy to top left pixel
newsurface = pygame.Surface((80,80))
myimage = newsurface.convert()
ckey = myimage.get_at((0,0))
myimage.set_colorkey(ckey, RLEACCEL)


#Lets create some text. We could use a loop, but lets keep it simple
font = pygame.font.Font(None, 220)
fontimg1 = font.render("12:34", 1, GRAY)
screen.blit(fontimg1, (0,0))
                  
while 1:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.quit()
            sys.exit(0)
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.display.quit()
            sys.exit(0)
        elif event.type == MOUSEBUTTONUP:
            pygame.display.quit()
            sys.exit(0)
    

    pygame.display.update() 
    pygame.time.delay(500)
