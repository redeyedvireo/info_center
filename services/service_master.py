from services.weather_service import WeatherService

class ServiceMaster:
    def __init__(self):
        self.modules = {}        # Holds the service modules
        self.uiManager = None

    def initServices(self, uiManager):
        self.uiManager = uiManager
        self._initService("weather", WeatherService(self, "weather"))

    def _initService(self, serviceId, serviceModule):
        self.modules[serviceId] = serviceModule
        serviceModule.initService()

    def getService(self, serviceId):
        return self.modules[serviceId]
