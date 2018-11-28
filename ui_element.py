# ui_element.py
#
# UiElement is the base class for all UI controls.

import pygame

class UiElement:
    def __init__(self, x, y, width, height, borderWidth):
        super(UiElement, self).__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.borderWidth = borderWidth

    def size(self):
        return self.rect.size
    
    def pos(self):
        return self.rect.x, self.rect.y

    def move(self, newX, newY):
        """ Moves the element to a new position. """
        self.rect = self.rect.move(newX, newY)

    def draw(self, pygame, screen):
        if self.borderWidth > 0:
            pygame.draw.rect(screen, (255, 255, 255), self.rect, self.borderWidth)

    def setNormal(self):
        """ To be overridden by subclasses. """
        pass

    def setPressed(self):
        """ To be overridden by subclasses. """
        pass

    def update(self, pygame, screen):
        """ Updates the UI element.  Subclasses can override as needed. """
        pass
