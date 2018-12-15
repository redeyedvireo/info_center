# ui_text_layout_item.py
#
# A layout item for text.

from ui_layout_item import UiLayoutItem


class UiTextLayoutItem(UiLayoutItem):
    def __init__(self, layout, hAlignment, text, color, fontSize):
        super(UiTextLayoutItem, self).__init__(layout, hAlignment)
        self.text = text
        self.color = color
        self.fontSize = fontSize
        self.font = None
        self.textImg = None

    def computeRect(self, pygame):
        """ Renders the text, so that the bounding rect may be determined. """
        self.font = pygame.font.Font(None, self.fontSize)
        self.width, self.height = self.font.size(self.text)

    def draw(self, screen, pos):
        if self.textImg is None:
            self.textImg = self.font.render(self.text, 1, self.color)
        screen.blit(self.textImg, pos)

