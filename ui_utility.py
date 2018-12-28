# ui_utility.py
#
# Utility functions.

# TODO: Maybe this should be part of UiManager.


import os
import pygame

scriptDir = os.path.dirname(os.path.realpath(__file__))


class UiUtility:
    def __init__(self):
        pass

    @staticmethod
    def loadImage(fileName):
        """ Loads an image from the images directory. """
        return pygame.image.load(os.path.join(scriptDir, "images", fileName)).convert()
