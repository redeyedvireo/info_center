# weather_panel.py
#
# A panel that displays the current weather conditions.

import pygame
from ui_panel import UiPanel
from downloader import Downloader
from datetime import datetime
from ui_layout import UiLayout
from ui_text_layout_item import UiTextLayoutItem
from ui_graphic_layout_item import UiGraphicLayoutItem
from ui_alignment import UiAlignment
from weather_icon_mapper import WeatherIconMapper
from ui_utility import UiUtility
from ui_colors import UiColors
import io


class WeatherPanel(UiPanel):
    def __init__(self, x, y, width, height, borderWidth, unpressedBackground, pressedBackground, onClickedFunc):
        super(WeatherPanel, self).__init__(x, y, width, height, True, borderWidth, unpressedBackground, pressedBackground, onClickedFunc)
        self.currentConditions = "Unknown conditions..."
        self.currentTemp = 0
        self.minTemp = 0
        self.maxTemp = 0
        self.sunrise = 0
        self.sunset = 0
        self.city = "Unknown"
        self.iconName = None
        self.weatherIconId = 0
        self.icon = None
        self.needsUpdate = True
        self.weatherService = None

    def init(self, uiManager):
        super(WeatherPanel, self).init(uiManager)
        self.weatherService = uiManager.getService("weather")
        self.weatherService.registerListener(self)
        self.serviceUpdate("weather")        # The service may have updated by this time

    def draw(self, pygame, screen):
        super(WeatherPanel, self).draw(pygame, screen)

        # Use UiLayout
        layout = UiLayout(self.rect, 5)
        layout.start()
        layout.addItem(UiTextLayoutItem(layout, UiAlignment.RIGHT, "{:5.0f} F".format(self.currentTemp), UiColors.GRAY, 90))
        layout.newLine()
        layout.addItem(UiGraphicLayoutItem(layout, UiAlignment.RIGHT, self.icon))
        layout.newLine()
        layout.addItem(UiTextLayoutItem(layout, UiAlignment.RIGHT, self.currentConditions, UiColors.GRAY, 40))

        layout.draw(pygame, screen)

    def serviceUpdate(self, serviceId):
        """ This is called from the service when the weather is updated. """
        self.currentConditions = self.weatherService.currentConditions
        self.currentTemp = self.kelvinToFahrenheight(self.weatherService.currentTemp)
        self.minTemp = self.kelvinToFahrenheight(self.weatherService.minTemp)
        self.maxTemp = self.kelvinToFahrenheight(self.weatherService.maxTemp)
        self.sunrise = self.weatherService.sunrise
        self.sunset = self.weatherService.sunset
        self.city = self.weatherService.city
        self.iconName = self.weatherService.iconName
        self.weatherIconId = self.weatherService.weatherIconId

        self.fetchIcon(self.iconName)

    def formatTime(self, time):
        timeStr = time.strftime("%I:%M %p")
        return timeStr

    def kelvinToFahrenheight(self, kelvin):
        return (kelvin - 273.15) * 9.0 / 5.0 + 32.0

    def fetchIcon(self, iconName):
        iconFileName = None

        if self.weatherIconId >= 200:
            iconFileName, description = WeatherIconMapper.convertIcon(self.weatherIconId, self.sunrise.time(), self.sunset.time())
            print("Icon file name: {}, Description: {}".format(iconFileName, description))

        if iconFileName is not None:
            self.icon = UiUtility.loadWeatherIcon(iconFileName)
            self.icon.fill(UiColors.GRAY, special_flags=pygame.BLEND_RGB_ADD)

        else:
            # This weather icon ID is not mapped to a weather icon.  In this case,
            # fetch the icon from OpenWeatherMap
            downloader = Downloader(None)

            # TODO: Do in either a background thread, or a coroutine
            url = "http://openweathermap.org/img/w/{}.png".format(iconName)
            downloader.download(url)

            image = downloader.getData()

            # Does image need to be processed before it can be used by Pygame?
            memFileObj = io.BytesIO(image)

            self.icon = pygame.image.load(memFileObj)

    def update(self, pygame, screen):
        """ Updates the weather.  Redraws, as necessary. """
        if self.needsUpdate:
            self.needsUpdate = False
            self.draw(pygame, screen)
