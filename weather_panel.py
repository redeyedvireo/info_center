# weather_panel.py
#
# A panel that displays the current time.

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
import json
import io


class WeatherPanel(UiPanel):
    WEATHER_TIMER = "weather_timer"

    def __init__(self, x, y, width, height, borderWidth, unpressedBackground, pressedBackground, appid, zipcode):
        super(WeatherPanel, self).__init__(x, y, width, height, True, borderWidth, unpressedBackground, pressedBackground)
        self.appid = appid
        self.zipcode = zipcode
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

    def init(self, uiManager):
        super(WeatherPanel, self).init(uiManager)
        uiManager.setTimer(timerId=self.WEATHER_TIMER, minutes=15, callback=self.fetchCurrentConditions)
        self.fetchCurrentConditions()

    def draw(self, pygame, screen):
        super(WeatherPanel, self).draw(pygame, screen)

        # Use UiLayout
        layout = UiLayout(self.rect, 5)
        layout.start()
        layout.addItem(UiTextLayoutItem(layout, UiAlignment.RIGHT, "{:5.0f} F".format(self.currentTemp), UiColors.GRAY, 70))
        layout.newLine()
        layout.addItem(UiGraphicLayoutItem(layout, UiAlignment.RIGHT, self.icon))
        layout.newLine()
        layout.addItem(UiTextLayoutItem(layout, UiAlignment.RIGHT, self.currentConditions, UiColors.GRAY, 40))

        layout.draw(pygame, screen)

    def fetchCurrentConditions(self):
        """ Fetches current conditions from the weather server. """
        downloader = Downloader(None)

        # TODO: Determine how to use async/await.  But, make sure this will run on the version of Python that is
        # present on the Raspberry Pi.
        url = "http://api.openweathermap.org/data/2.5/weather?zip={},us&APPID={}".format(self.zipcode, self.appid)
        downloader.download(url)

        weatherJson = downloader.getDataAsString()
        self.parseWeatherJson(weatherJson)

        self.fetchIcon(self.iconName)

    def parseWeatherJson(self, weatherJson):
        print(weatherJson)

        jsonObj = json.loads(weatherJson)
        self.city = jsonObj['name']
        weatherObj = jsonObj['weather']
        self.currentConditions = weatherObj[0]['main']

        mainObj = jsonObj['main']
        currentTempKelvin = float(mainObj['temp'])
        minTempKelvin = float(mainObj['temp_min'])
        maxTempKelvin = float(mainObj['temp_max'])

        self.currentTemp = self.kelvinToFahrenheight(currentTempKelvin)
        self.minTemp = self.kelvinToFahrenheight(minTempKelvin)
        self.maxTemp = self.kelvinToFahrenheight(maxTempKelvin)

        sysObj = jsonObj['sys']
        sunrise = int(sysObj['sunrise'])
        sunset = int(sysObj['sunset'])
        self.sunrise = datetime.fromtimestamp(sunrise)
        self.sunset = datetime.fromtimestamp(sunset)

        self.iconName = weatherObj[0]['icon']
        self.weatherIconId = weatherObj[0]['id']

        print("City: {}, conditions: {}, icon: {}, icon ID: {}".format(self.city, self.currentConditions, self.iconName, self.weatherIconId))
        print("Current temp: {}, Min temp: {}, Max temp: {}".format(self.currentTemp, self.minTemp, self.maxTemp))
        print("Sunrise: {}, Sunset: {}".format(self.formatTime(self.sunrise), self.formatTime(self.sunset)))

    def formatTime(self, time):
        timeStr = time.strftime("%I:%M %p")
        return timeStr

    def kelvinToFahrenheight(self, kelvin):
        return (kelvin - 273.15) * 9.0 / 5.0 + 32.0

    def fetchIcon(self, iconName):
        iconFileName = None

        if self.weatherIconId >= 200:
            iconFileName, description = WeatherIconMapper.convertIcon(self.weatherIconId)
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
