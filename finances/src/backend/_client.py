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

        if not self.isConnected():
            result['error'] = 'server not connected'
            return result
        
        credentials = {
            'username': username,
            'password': password,
        }
        
        response = self.__session.post(SERVER_IP+'/auth/login', credentials, headers={'X-CSRFToken': self.__token})
        code = response.status_code

        match code:
            case 400:
                data = response.json()
                result['error'] = data['message']

            case 200:
                result['success'] = True
            
            case _:
                raise ValueError(f'undefined code response {code} to /auth/login')

        return result
    
    def logout(self):
        self.__session.get(SERVER_IP+'/auth/logout')
    
    def getUserData(self) -> dict | None:
        if not self.isConnected():
            return
        
        response = self.__session.get(SERVER_IP+'/data/session')
        if response.status_code == 401:
            return
        
        return response.json()
    
    def createAccount(self, data:dict) -> dict:
        response = self.__session.post(SERVER_IP+'/auth/create_user', data, headers={'X-CSRFToken': self.__token})
        result = {'success': False, 'error': ''}
        code = response.status_code
        
        match code:
            case 400:
                data = response.json()
                result['error'] = data['message']

            case 200:
                result['success'] = True
            
            case _:
                raise ValueError(f'undefined code response {code} to /auth/create_user')

        return result
