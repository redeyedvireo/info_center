# ui_utility.py
#
# Utility functions.

# TODO: Maybe this should be part of UiManager.


import os
import pygame
from ui_colors import UiColors
from ui_alignment import UiAlignment


scriptDir = os.path.dirname(os.path.realpath(__file__))


class UiUtility:
    def __init__(self):
        pass

    @staticmethod
    def loadImage(fileName):
        """ Loads an image from the images directory. """
        return UiUtility._loadImage(os.path.join(scriptDir, "images", fileName))

    @staticmethod
    def loadWeatherIcon(fileName):
        """ Loads a weather icon. """
        return UiUtility._loadImage(os.path.join(scriptDir, "weather", fileName))

    @staticmethod
    def _loadImage(filePath):
        return pygame.image.load(filePath).convert_alpha()

    @staticmethod
    def drawText(pygame, screen, pos, text, fontSize, hAlign = None, vAlign = None, box = None):
        """ Draws the given text, at the given position, with the given font size.
            Alignment within a box can be performed if box and hAlignment and/or vAlignment is provided.
            Either hAlign or vAlign can be None if alignment is not needed in either direction.
            box must not be None if either hAlign or vAlign is not None.  box is a pygame rect.  If
            box is provided, pos is not used. """
        font = pygame.font.Font(None, fontSize)
        image = font.render(text, 1, UiColors.GRAY)
        x = pos[0]
        y = pos[1]

        if hAlign is not None:
            if hAlign == UiAlignment.RIGHT:
                x = box.right - image.get_width()
            elif hAlign == UiAlignment.HCENTER:
                x = box.left + (box.width - image.get_width()) / 2

        if vAlign is not None:
            if vAlign == UiAlignment.BOTTOM:
                y = box.bottom - image.get_height()
            elif vAlign == UiAlignment.VCENTER:
                y = box.top + (box.height - image.get_height()) / 2

        newPos = x, y
        screen.blit(image, newPos)
        return image
