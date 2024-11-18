from PySide6.QtCore import QObject, Signal
from threading import Thread
import os
from queue import Queue
from configparser import ConfigParser

from .._consts import *
from .._tools import queueWorker
from ._appevents import AppEventHandler
from ._client import ClientServer

class AppModel(QObject):
    initializationFinished = Signal(dict)
    
    def __init__(self, events:AppEventHandler):
        super().__init__()
        self.__events = events
        self.__client = ClientServer()
        self.__userCredentials = {}
        self.__saveCredentials = None # definido em initialize
        self.__userId = -1
        self.__userData = {}

        self.__threads = Queue()
        Thread(target=queueWorker, args=(self.__threads, ), daemon=True).start()
        
        # slots
        self.__events.loginRequired.connect(self.on_loginRequired)
        self.__events.loginFinished.connect(self.on_loginFinished)
        self.__events.userDataUpdated.connect(self.on_userDataUpdated)

    def initialize(self):
        self.__threads.put((self.__initialize, [], dict(signal_done=self.initializationFinished, signal_with_result=True)))
    
    def remember(self) -> bool:
        return self.__saveCredentials
    
    def setRemember(self, __arg1:bool):
        self.__saveCredentials = __arg1

    def savedCredentials(self) -> dict:
        return self.__userCredentials

    def saveCredentials(self, __arg1:bool=True):
        self.setRemember(__arg1)
        username = self.__userCredentials.get('username', '') if __arg1 else ''
        password = self.__userCredentials.get('password', '') if __arg1 else ''

        self.updateConfig({
            'Authentication': {
                'remember': str(__arg1),
            },
            'Authentication.credentials': {
                'username': username,
                'password': password,
            },
        })
        
    def updateConfig(self, values:dict={}):
        self.__config.update(values)
        with open(FILE_SETTINGS, 'w') as f:
            self.__config.write(f)

    def __initialize(self):
        os.makedirs(PATH_TEMP, exist_ok=True)
        self.__config = ConfigParser()

        if os.path.exists(FILE_SETTINGS):
            with open(FILE_SETTINGS) as f:
                self.__config.read_file(f)
        else:
            self.updateConfig(DEFAULT_SETTINGS)

        self.__saveCredentials = self.__config['Authentication']['remember'] == 'True'
        self.__userCredentials = dict(self.__config['Authentication.credentials'])

        return self.__client.connect()

    def on_loginRequired(self, credentials:dict):
        # self.__events.loginFinished.emit(self.__client.login(credentials['username'], credentials['password']))
        self.__userCredentials = credentials
        self.__threads.put((
            self.__client.login,
            [],
            dict(**credentials, signal_done=self.__events.loginFinished, signal_with_result=True)
        ))

    def on_loginFinished(self, result:dict):
        if result['success']:
            self.saveCredentials(self.remember())
            self.__userId = result['userId']

            self.__threads.put((
                self.__client.getUserData,
                [self.__userId],
                dict(signal_done=self.__events.userDataUpdated, signal_with_result=True)
            ))
        
    def on_userDataUpdated(self, data:dict):
        self.__userData = data

    def on_quitRequired(self):
        self.__threads.join()