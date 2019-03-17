# ui_textutils.py
#
# Text utilities.

import operator
import logging
from ui_alignment import UiAlignment


class TextUtil:
    def __init__(self):
        pass

    @staticmethod
    def drawText(pygame, screen, text, color, fontSize, hAlignment, pos, totalWidth):
        """ Draws the given text with the given parameters.
            A bounding rect of the text is returned. """
        font = pygame.font.Font(None, fontSize)
        img = font.render(text, 1, color)

        if hAlignment == UiAlignment.LEFT:
            destPos = pos
        elif hAlignment == UiAlignment.RIGHT:
            destPos = tuple(map(operator.add, pos, (totalWidth - img.get_width(), 0)))
        elif hAlignment == UiAlignment.CENTER:
            destPos = tuple(map(operator.add, pos, ((totalWidth - img.get_width()) / 2, 0)))
        else:
            # Unknown alignment constant
            logging.error("drawText: Unknown alignment constant: {}".format(hAlignment))
            return

        screen.blit(img, destPos)
        return img.get_rect()
