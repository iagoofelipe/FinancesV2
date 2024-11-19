import os
import sys
from PySide6.QtGui import QFont

__id = -1
def generateId() -> int:
    global __id
    __id += 1
    return __id

__all__ = [
    'VERSION', 'DEFAULT_SETTINGS', 'WINDOW_WIDTH', 'WINDOW_HEIGHT', 'WINDOW_TITLE', 'FONT',
    'SERVER_IP',
    'PATH_TEMP',
    'FILE_SETTINGS',
    'WID_ID_LOADING', 'WID_ID_LOGIN', 'WID_ID_CREATE_ACCOUNT', 'WID_ID_HOME', 'USER_DEFAULT_DATA', 'LOADING_MESSAGE',
    'COMPONENT_HOME_DASHBOARD', 'COMPONENT_HOME_REGISTRY', 'COMPONENT_HOME_CARD', 'COMPONENTS_HOME',
]

# Others
VERSION = '1.0.0'
DEFAULT_SETTINGS = {
    'Authentication': {'remember': 'False'},
    'Authentication.credentials': {'username': '', 'password': ''},
}
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 670
WINDOW_TITLE = 'Finances'
FONT = QFont()
FONT.setFamilies([u".AppleSystemUIFont"] if sys.platform == 'darwin' else [u"Calibri"])
FONT.setPointSize(12)

# Server
SERVER_IP = 'http://192.168.1.19:443'

# Path
PATH_TEMP = os.path.join(os.environ.get('TEMP', '.temp'), f'Finances_{VERSION}')

# Files
FILE_SETTINGS = os.path.join(PATH_TEMP, 'settings.ini')

# UIs
WID_ID_LOADING = generateId()
WID_ID_LOGIN = generateId()
WID_ID_CREATE_ACCOUNT = generateId()
WID_ID_HOME = generateId()
USER_DEFAULT_DATA = { 'name': 'Usuário' }

LOADING_MESSAGE = 'carregando componentes...'

COMPONENT_HOME_DASHBOARD = generateId()
COMPONENT_HOME_REGISTRY = generateId()
COMPONENT_HOME_CARD = generateId()
COMPONENTS_HOME = [COMPONENT_HOME_DASHBOARD, COMPONENT_HOME_REGISTRY, COMPONENT_HOME_CARD]