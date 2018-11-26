# time_panel.py
#
# A panel that displays the current time.

from ui_panel import UiPanel

# GRAY = 20, 20, 20
GRAY = 120, 120, 120


class TimePanel(UiPanel):
    def __init__(self, x, y, width, height, borderWidth):
        super(TimePanel, self).__init__(x, y, width, height, True, borderWidth)

    def draw(self, pygame, screen):
        super(TimePanel, self).draw(pygame, screen)
        font = pygame.font.Font(None, 220)
        fontimg = font.render("12:34", 1, GRAY)
        screen.blit(fontimg, self.pos())
