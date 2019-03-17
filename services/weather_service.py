import pygame
from datetime import datetime
import configparser
import json
import io
import logging
from services.service_base import ServiceBase
from downloader import Downloader


CONFIG_FILE = 'info_center.ini'

class WeatherService(ServiceBase):
    WEATHER_TIMER = "weather_timer"

    def __init__(self, serviceMaster, serviceId):
        super(WeatherService, self).__init__(serviceMaster, serviceId)
        self.zipcode = ""
        self.weatherAppId = ""
        self.currentConditions = "Unknown conditions..."
        self.currentTemp = 0    # Current temperature, in Kelvin
        self.minTemp = 0        # Min temperature, in Kelvin
        self.maxTemp = 0        # Max temperature, in Kelvin
        self.sunrise = 0
        self.sunset = 0
        self.city = "Unknown"
        self.iconName = None
        self.weatherIconId = 0

    def initService(self):
        self.readConfig()
        self.serviceMaster.uiManager.setTimer(timerId=self.WEATHER_TIMER, minutes=15, callback=self.fetchCurrentConditions)
        self.fetchCurrentConditions()

    def readConfig(self):
        """ Reads the config file.  For now, only the weather config is returned. """
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE)

        self.zipcode = config['weather']['zipcode']
        self.weatherAppId = config['weather']['appid']

    def fetchCurrentConditions(self):
        """ Fetches current conditions from the weather server. """
        downloader = Downloader(None)

        # TODO: Determine how to use async/await.  But, make sure this will run on the version of Python that is
        # present on the Raspberry Pi.
        url = "http://api.openweathermap.org/data/2.5/weather?zip={},us&APPID={}".format(self.zipcode, self.weatherAppId)
        if not downloader.download(url):
            # Error occurred in downloading weather data.
            logging.error("fetchCurrentConditions: Error occurred in downloading weather data.")
            return

        weatherJson = downloader.getDataAsString()
        self.parseWeatherJson(weatherJson)

        self.fetchIcon(self.iconName)

        self._notifyListeners()

    def parseWeatherJson(self, weatherJson):
        if weatherJson is None:
            logging.error("weatherJson is None")
            return

        print(weatherJson)

        jsonObj = json.loads(weatherJson)
        self.city = jsonObj['name']
        weatherObj = jsonObj['weather']
        self.currentConditions = weatherObj[0]['main']

        mainObj = jsonObj['main']
        self.currentTemp = float(mainObj['temp'])       # In Kelvin
        self.minTemp = float(mainObj['temp_min'])       # In Kelvin
        self.maxTemp = float(mainObj['temp_max'])       # In Kelvin

        sysObj = jsonObj['sys']
        sunrise = int(sysObj['sunrise'])
        sunset = int(sysObj['sunset'])
        self.sunrise = datetime.fromtimestamp(sunrise)
        self.sunset = datetime.fromtimestamp(sunset)

        self.iconName = weatherObj[0]['icon']
        self.weatherIconId = weatherObj[0]['id']

        print("City: {}, conditions: {}, icon: {}, icon ID: {}".format(self.city, self.currentConditions, self.iconName, self.weatherIconId))
        print("Current temp: {}, Min temp: {}, Max temp: {}".format(self.currentTemp, self.minTemp, self.maxTemp))
        print("Sunrise: {}, Sunset: {}".format(self.sunrise, self.sunset))

    def fetchIcon(self, iconName):
        """ Fetch the icon from the internet, even if it ends up not being used. """

        if iconName is None or len(iconName) == 0:
            logging.error("fetchIcon: iconName is either None or empty.")
            return

        # This weather icon ID is not mapped to a weather icon.  In this case,
        # fetch the icon from OpenWeatherMap
        downloader = Downloader(None)

        # TODO: Do in either a background thread, or a coroutine
        url = "http://openweathermap.org/img/w/{}.png".format(iconName)
        if not downloader.download(url):
            # Error occurred in downloading.  Abort.
            logging.error("fetchIcon: Error occurred in downloading icon.")
            return

        image = downloader.getData()

        if image is not None:
            # Does image need to be processed before it can be used by Pygame?
            memFileObj = io.BytesIO(image)

            self.icon = pygame.image.load(memFileObj)
