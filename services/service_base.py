
class ServiceBase:
    def __init__(self, serviceMaster, serviceId):
        self.listeners = []
        self.serviceId = serviceId
        self.serviceMaster = serviceMaster

    def registerListener(self, listener):
        self.listeners.append(listener)

    def _notifyListeners(self):
        for listener in self.listeners:
            # Send the service ID in the serviceUpdate call in case the client is
            # subscribed to more than one service.
            listener.serviceUpdate(self.serviceId)

