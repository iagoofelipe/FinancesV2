import requests

from .._consts import SERVER_IP

class ClientServer:
    def __init__(self):
        self.__session = requests.Session()
        self.__token:str = None
        self.__connected = False

    def connect(self) -> dict:
        self.__token = None
        self.__connected = False

        try:
            response = self.__session.get(SERVER_IP+'/auth/token')
        except requests.exceptions.ConnectionError:
            return {'success': False, 'error': "couldn't connect with the server, ConnectionError"}
        
        if response.status_code != 200:
            return {'success': False, 'error': "couldn't connect with the server, ServerError"}

        self.__token = response.cookies.get('csrftoken')
        if not self.__token:
            return {'success': False, 'error': "couldn't get the token"}

        self.__connected = True
        return {'success': True, 'error': ""}
    
    def isConnected(self) -> bool:
        return self.__connected
    
    def login(self, username:str, password:str) -> dict:
        result = {'success': False, 'error': ''}

        if not self.__connected:
            result['error'] = 'server not connected'
            return result
        
        credentials = {
            'username': username,
            'password': password,
        }
        
        response = self.__session.post('http://127.0.0.1:8000/auth/login', credentials, headers={'X-CSRFToken': self.__token})
        return response.json()