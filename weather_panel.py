# weather_panel.py
#
# A panel that displays the current time.

from ui_panel import UiPanel
from downloader import Downloader
from datetime import datetime
from ui_layout import UiLayout
from ui_text_layout_item import UiTextLayoutItem
from ui_graphic_layout_item import UiGraphicLayoutItem
from ui_space_layout_item import UiSpaceLayoutItem
from ui_alignment import UiAlignment
from ui_textutils import TextUtil
import operator
import json
import io

# TODO: Put all color constants in a global file.
GRAY = 80, 80, 80


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
        self.image = None
        self.icon = None
        self.needsUpdate = True

    def init(self, uiManager):
        super(WeatherPanel, self).init(uiManager)
        uiManager.setTimer(timerId=self.WEATHER_TIMER, minutes=15, callback=self.fetchCurrentConditions)
        self.fetchCurrentConditions()

    def draw(self, pygame, screen):
        super(WeatherPanel, self).draw(pygame, screen)

        # Icon
        if self.image is not None:
            # Does image need to be processed before it can be used by Pygame?
            memFileObj = io.BytesIO(self.image)

            self.icon = pygame.image.load(memFileObj)

        # Use UiLayout
        layout = UiLayout(self.rect, 5)
        layout.start()
        layout.addItem(UiTextLayoutItem(layout, UiAlignment.RIGHT, self.city, GRAY, 40))
        layout.newLine()
        layout.addItem(UiTextLayoutItem(layout, UiAlignment.RIGHT, self.currentConditions, GRAY, 30))
        layout.newLine()
        layout.addItem(UiGraphicLayoutItem(layout, UiAlignment.RIGHT, self.icon))
        layout.newLine()
        layout.addItem(UiSpaceLayoutItem(layout, 1, 25))
        layout.newLine()
        layout.addItem(UiTextLayoutItem(layout, UiAlignment.RIGHT, "Temp: {:5.1f}".format(self.currentTemp), GRAY, 30))
        layout.newLine()
        layout.addItem(UiTextLayoutItem(layout, UiAlignment.RIGHT, "Sunrise: {}".format(self.formatTime(self.sunrise)), GRAY, 30))
        layout.newLine()
        layout.addItem(UiTextLayoutItem(layout, UiAlignment.RIGHT, "Sunset: {}".format(self.formatTime(self.sunset)), GRAY, 30))

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
        downloader = Downloader(None)

        # TODO: Do in either a background thread, or a coroutine
        url = "http://openweathermap.org/img/w/{}.png".format(iconName)
        downloader.download(url)

        self.image = downloader.getData()

    def update(self, pygame, screen):
        """ Updates the weather.  Redraws, as necessary. """
        if self.needsUpdate:
            self.needsUpdate = False
            self.draw(pygame, screen)
