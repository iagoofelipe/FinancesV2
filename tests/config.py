from configparser import ConfigParser

config = ConfigParser()
with open('settings.ini') as f:
    config.read_file(f)

config['Authentication']['remember'] = 'False'

with open('settings.ini', 'w') as f:
    config.write(f)