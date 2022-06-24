# -*- coding: utf-8 -*-

"""
application_properties.py: The python file dedicated to the particular process of retrieving
the current Profile & current Profile's properties of the Project
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

import configparser

config = configparser.ConfigParser()
config.read('application.ini')
# retrieving the chosen Profile
profile = config['PROFILE']['value']


def get_application_property(property_key) -> str:
    """
    Getting an application's property from the latter's "property_key".

    :param property_key: The property key of the wanted property
    :return: The value of the wanted property
    """
    return config[profile][property_key]

