import os
from PySide6.QtGui import QFont

__all__ = [
    'VERSION', 'DEFAULT_SETTINGS', 'WINDOW_WIDTH', 'WINDOW_HEIGHT', 'FONT',
    'SERVER_IP',
    'PATH_TEMP',
    'FILE_SETTINGS',
    'WID_ID_LOADING', 'WID_ID_LOGIN', 'WID_ID_CREATE_ACCOUNT', 'WID_ID_HOME',
    'LOADING_MESSAGE'
]

# Others
VERSION = '1.0.0'
DEFAULT_SETTINGS = {
    'Authentication': {'remember': 'False'},
    'Authentication.credentials': {'username': '', 'password': ''},
}
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 670
FONT = QFont()
FONT.setFamilies([u"Calibri"])
FONT.setPointSize(12)

# Server
SERVER_IP = 'http://192.168.19:443'

# Path
PATH_TEMP = os.path.join(os.environ.get('TEMP', '.temp'), f'Finances_{VERSION}')

# Files
FILE_SETTINGS = os.path.join(PATH_TEMP, 'settings.ini')

# UIs
WID_ID_LOADING = 0
WID_ID_LOGIN = 1
WID_ID_CREATE_ACCOUNT = 2
WID_ID_HOME = 3

LOADING_MESSAGE = 'carregando componentes...'
