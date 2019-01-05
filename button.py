# button.py
#
# Button class.

from ui_element import UiElement
import pygame
from pygame import Surface
from ui_utility import UiUtility
from ui_colors import UiColors


class Button(UiElement):
    # Properties
    #  - unpressed image
    #  - pressed image
    #  - x
    #  - y
    #  - state - True if pressed, False if unpressed
    #  - getSurface - returns the button's image, depending on its state
    #  - onClicked - when button is clicked (pressed, then unpressed)
    #  - onPressed - when button pressed (ie, pushed in)
    #  - onReleased - when button released

    # Button states
    STATE_NORMAL = 0
    STATE_PRESSED = 1

    def __init__(self, x, y, normalImage, pressedImage, onClickedFunc, borderWidth):
        normalImageWidth, normalImageHeight = normalImage.get_size()
        pressedImageWidth, pressedImageHeight = pressedImage.get_size()

        width = max(normalImageWidth, pressedImageWidth)
        height = max(normalImageHeight, pressedImageHeight)

        super(Button, self).__init__(x, y, width, height, borderWidth)
        self.normalImage = normalImage
        self.pressedImage = pressedImage
        self.state = self.STATE_NORMAL
        self.onClickedFunc = onClickedFunc

    @staticmethod
    def createSolidButton(x, y, width, height, colorNormal, colorPressed, onClickedFunc):
        """ Creates a solid button, where colorNormal is the normal, unpressed color, and
            colorPressed is the pressed color.
             colorNormal and colorPressed are tuples, containing red, blue, green. """
        normalSurface = Surface((width, height))
        normalImage = normalSurface.convert()
        normalImage.fill(colorNormal)
        pressedSurface = Surface((width, height))
        pressedImage = pressedSurface.convert()
        pressedImage.fill(colorPressed)

        return Button(x, y, normalImage, pressedImage, onClickedFunc, 0)

    @staticmethod
    def createButton(x, y, normalImageFileName, pressedImageFileName, onClickedFunc):
        """ Creates a button with normal and pressed images. """
        normalImage = UiUtility.loadImage(normalImageFileName)
        pressedImage = UiUtility.loadImage(pressedImageFileName)

        return Button(x, y, normalImage, pressedImage, onClickedFunc, 0)

    @staticmethod
    def createButtonWithAutoPressed(x, y, normalImageFileName, foregroundColor, onClickedFunc):
        """ Creates a button with normal and pressed images.  The pressed image is generated automatically.
            The foregroundColor parameter allows the button to be colored with the given color.  This only works if
            the button's background is transparent.  This can be set to None to avoid this behavior. """
        normalImage = UiUtility.loadImage(normalImageFileName)
        if foregroundColor is not None:
            normalImage.fill(UiColors.GRAY, special_flags=pygame.BLEND_RGB_ADD)

        pressedImage = Surface((normalImage.get_width(), normalImage.get_height()))
        pressedImage.fill((255, 255, 255))

        # Ooops - add is not right.  Want to replace the existing non-transparent pixels with the new ones.
        pressedImage.blit(normalImage, (0, 0), special_flags=pygame.BLEND_RGB_MIN)

        return Button(x, y, normalImage, pressedImage, onClickedFunc, 0)

    def draw(self, pygame, screen):
        super(Button, self).draw(pygame, screen)
        screen.blit(self.getSurface(), self.pos())

    def getNormal(self):
        return self.normalImage

    def getPressed(self):
        return self.pressedImage

    def getSurface(self):
        if self.state == self.STATE_NORMAL:
            return self.normalImage
        else:
            return self.pressedImage

    def setNormal(self):
        self.state = self.STATE_NORMAL
        self.onReleased()

    def setPressed(self):
        self.state = self.STATE_PRESSED
        self.onPressed()

    def onClicked(self):
        if self.onClickedFunc is not None:
            self.onClickedFunc()

    #
    # ************ OVERRIDABLES ************
    #
    def onPressed(self):
        pass

    def onReleased(self):
        pass
