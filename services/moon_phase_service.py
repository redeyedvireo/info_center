import pygame
from datetime import datetime
from downloader import Downloader
from services.service_base import ServiceBase
import json


class MoonPhaseService(ServiceBase):
    MOONPHASE_TIMER = "moonphase_timer"

    def __init__(self, serviceMaster, serviceId):
        super(MoonPhaseService, self).__init__(serviceMaster, serviceId)
        self.moonPhase = "Moon Phase"
        self.moonPhaseIconIndex = 0

    def initService(self):
        self.serviceMaster.uiManager.setTimer(timerId=self.MOONPHASE_TIMER, hours=6, callback=self.fetchCurrentMoonPhase)
        self.fetchCurrentMoonPhase()

    def fetchCurrentMoonPhase(self):
        downloader = Downloader(None)

        currentTimestamp = datetime.now().timestamp()

        url = "http://api.farmsense.net/v1/moonphases/?d={}".format(int(currentTimestamp))
        downloader.download(url)

        moonPhaseJson = downloader.getDataAsString()
        self.parseMoonPhaseJson(moonPhaseJson)
        self._notifyListeners()

    def parseMoonPhaseJson(self, moonPhaseJson):
        print(moonPhaseJson)

        jsonObj = json.loads(moonPhaseJson)
        mainMoonPhaseObj = jsonObj[0]
        self.moonPhase = mainMoonPhaseObj["Phase"]

        self.moonPhaseIconIndex = int(mainMoonPhaseObj["Index"])
        print("Moon icon index: {}".format(self.moonPhaseIconIndex))

