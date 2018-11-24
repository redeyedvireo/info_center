# ui_element.py
#
# UiElement is the base class for all UI controls.

import pygame

class UiElement:
    def __init__(self, x, y, width, height):
        super(UiElement, self).__init__()
        self.rect = pygame.Rect(x, y, width, height)

    def size(self):
        return self.width, self.height
    
    def pos(self):
        return self.rect.x, self.rect.y

    def move(self, newX, newY):
        """ Moves the element to a new position. """
        self.rect = self.rect.move(newX, newY)
