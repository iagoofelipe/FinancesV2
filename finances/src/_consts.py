import os

__all__ = [
    'VERSION', 'DEFAULT_SETTINGS',
    'SERVER_IP',
    'PATH_TEMP',
    'FILE_SETTINGS'
]

# Others
VERSION = '1.0.0'
DEFAULT_SETTINGS = {
    'Authentication': {'remember': 'False'},
    'Authentication.credentials': {'username': '', 'password': ''},
}

# Server
SERVER_IP = 'http://127.0.0.1:8000'

# Path
PATH_TEMP = os.path.join(os.environ.get('TEMP', '.'), f'Finances_{VERSION}')

# Files
FILE_SETTINGS = os.path.join(PATH_TEMP, 'settings.ini')
