import requests_async as requests
from PySide6.QtCore import QObject, Signal
import asyncio

__all__ = ['MainModel']

class MainModel(QObject):
    initializationFinished = Signal(dict)

    def __init__(self):
        super().__init__()
        self.__token:str = None
        self.__session = requests.Session()

    async def initialize(self):
        await asyncio.sleep(3)
        
        result = { 'success': False, 'error': "" }
        self.__token = None
        
        try:
            response = await self.__session.get('http://127.0.0.1:8000/auth/')
            code = response.status_code
            self.__token = response.cookies.get('csrftoken')

        except requests.exceptions.ConnectionError:
            code = 400

        if code != 200:
            result['error'] = "couldn't connect with the server"
        
        elif not self.__token:
            result['error'] = "couldn't extract the token"

        else:
            result['success'] = True

        self.initializationFinished.emit(result)
