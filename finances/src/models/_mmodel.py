import asyncio
from PySide6.QtCore import QObject
import requests_async as requests

__all__ = ['MainModel']

class MainModel(QObject):
    def __init__(self) -> None:
        super().__init__()
        self.__session = requests.Session()
        self.__token:str = None
    
    async def initialize(self) -> tuple[bool, str]:
        self.__token = None

        try:
            response = await requests.get('http://127.0.0.1:8000/auth/')
            code = response.status_code
            self.__token = response.cookies.get('csrftoken')

        except Exception as e:
            print(e)
            return (False, "couldn't connect with the server, ConnectionError")
        
        if code != 200:
            return (False, "couldn't connect with the server, ServerError")

        if not self.__token:
            return (False, "couldn't get the token")

        print('MainModel inicializado')
        r = (True, "ewww")
        return r
        