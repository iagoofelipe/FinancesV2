from PySide6.QtCore import QObject, Signal
from threading import Thread

from ._appevents import AppEventHandler
from ._client import ClientServer

class AppModel(QObject):
    initializationFinished = Signal(dict)
    
    def __init__(self, events:AppEventHandler):
        super().__init__()
        self.__events = events
        self.__client = ClientServer()

        self.__events.loginRequired.connect(self.on_loginRequired)

    def initialize(self):
        Thread(target=self.__initialize).start()

    def __initialize(self):
        success, error = self.__client.connect()
        result = dict(success=success, error=error)

        self.initializationFinished.emit(result)

    def on_loginRequired(self, credentials:dict):
        self.__events.loginFinished.emit(self.__client.login(credentials['username'], credentials['password']))