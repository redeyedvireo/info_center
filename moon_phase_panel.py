# moon_phase_panel.py
#
# A panel that displays the moon phase for the current day.

import pygame
from ui_panel import UiPanel
from downloader import Downloader
from datetime import datetime
from ui_layout import UiLayout
from ui_text_layout_item import UiTextLayoutItem
from ui_graphic_layout_item import UiGraphicLayoutItem
from ui_alignment import UiAlignment
from ui_utility import UiUtility
from ui_colors import UiColors
import json
import io


class MoonPhasePanel(UiPanel):

    def __init__(self, x, y, width, height, borderWidth, unpressedBackground, pressedBackground, onClickedFunc):
        super(MoonPhasePanel, self).__init__(x, y, width, height, True, borderWidth, unpressedBackground, pressedBackground, onClickedFunc)

        self.moonPhase = "Moon Phase"
        self.icon = None
        self.moonPhaseIconIndex = 0
        self.moonPhaseService = None

    def init(self, uiManager):
        super(MoonPhasePanel, self).init(uiManager)
        self.moonPhaseService = uiManager.getService("moonphase")
        self.moonPhaseService.registerListener(self)
        self.serviceUpdate("moonphase")

    def draw(self, pygame, screen):
        super(MoonPhasePanel, self).draw(pygame, screen)

        layout = UiLayout(self.rect, 5)
        layout.start()
        layout.addItem(UiTextLayoutItem(layout, UiAlignment.RIGHT, self.moonPhase, UiColors.GRAY, 60))
        if self.icon is not None:
            layout.newLine()
            layout.addItem(UiGraphicLayoutItem(layout, UiAlignment.RIGHT, self.icon))

        layout.draw(pygame, screen)

    def serviceUpdate(self, serviceId):
        """ This is called from the service when the moon phase is updated. """
        self.moonPhase = self.moonPhaseService.moonPhase
        moonPhaseIconIndex = self.moonPhaseService.moonPhaseIconIndex
        self.fetchMoonPhaseIcon(moonPhaseIconIndex)

    def fetchMoonPhaseIcon(self, iconIndex):
        iconFileName = None

        if iconIndex == 0:
            iconFileName = "wi-moon-new.png"    # Note: this won't show up on a black screen!

        elif iconIndex == 30 or iconIndex == 29:
            iconFileName = "wi-moon-new.png"

        elif iconIndex == 7:
            iconFileName = "wi-moon-first-quarter.png"

        elif iconIndex == 21:
            iconFileName = "wi-moon-third-quarter.png"

        elif iconIndex == 14:
            iconFileName = "wi-moon-full.png"

        elif iconIndex in range(1, 7):
            iconFileName = "wi-moon-waxing-crescent-{}.png".format(iconIndex)

        elif iconIndex in range(8, 14):
            iconFileName = "wi-moon-waxing-gibbous-{}.png".format(iconIndex-7)

        elif iconIndex in range(15, 21):
            iconFileName = "wi-moon-waning-gibbous-{}.png".format(iconIndex-14)

        elif iconIndex in range(22, 28):
            iconFileName = "wi-moon-waning-crescent-{}.png".format(iconIndex-21)

        elif iconIndex == 28:
            iconFileName = "wi-moon-waning-crescent-6.png"

        else:
            iconFileName = "wi-na.png"

        if iconFileName is not None:
            self.icon = UiUtility.loadWeatherIcon(iconFileName)
            self.icon.fill(UiColors.GRAY, special_flags=pygame.BLEND_RGB_ADD)



