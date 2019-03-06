# ui_graphic_layout_item.py
#
# A layout item for images.

from ui_layout_item import UiLayoutItem


class UiGraphicLayoutItem(UiLayoutItem):
    def __init__(self, layout, hAlignment, image):
        super(UiGraphicLayoutItem, self).__init__(layout, hAlignment)
        self.image = image      # Here, the image is a PyGame surface

    def computeRect(self, pygame):
        """ Renders the text, so that the bounding rect may be determined. """
        if self.image is not None:
            self.width = self.image.get_width()
            self.height = self.image.get_height()
        else:
            self.width = 0
            self.height = 0

    def draw(self, screen, pos):
        if self.image is not None:
            screen.blit(self.image, pos)
