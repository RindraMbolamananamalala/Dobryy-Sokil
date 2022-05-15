import configparser

config = configparser.ConfigParser()
config.read('application.ini')
profile = config['PROFILE']['value']


def get_application_property(property_key):
    return config[profile][property_key]

