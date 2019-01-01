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
        return UiUtility._loadImage(os.path.join(scriptDir, "images", fileName))

    @staticmethod
    def loadWeatherIcon(fileName):
        """ Loads a weather icon. """
        return UiUtility._loadImage(os.path.join(scriptDir, "weather", fileName))

    @staticmethod
    def _loadImage(filePath):
        return pygame.image.load(filePath).convert()
