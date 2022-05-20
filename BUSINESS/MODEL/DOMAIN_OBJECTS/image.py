# -*- coding: utf-8 -*-

"""
image.py: The python file dedicated to the "Model:Image" part of the MVC pattern implemented within
the "BUSINESS" layer of the Project, and at the same time one of the Project's DOs
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

from BUSINESS.MODEL.DOMAIN_OBJECTS.dobryy_sokil_DO import DobryySokilDO


class Image(DobryySokilDO):

    def set_location_path(self, location_path: str):
        self.location_path = location_path

    def get_location_path(self) -> str:
        return self.location_path

    def set_name(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_extension(self, extension: str):
        self.extension = extension

    def get_extension(self) -> str:
        return self.extension

    def get_absolute_path(self) -> str:
        """

        :return: The absolute path of the file containing the Image
        """
        return self.get_location_path().replace("/", "\\") \
               + "\\" \
               + self.get_name() \
               + "." \
               + self.get_extension()

    def __init__(self
                 , location_path: str
                 , name: str
                 , extension: str):
        """

        :param location_path: The path of the directory where the file containing the Image is located
        :param name: The filename of the file containing the Image
        :param extension: The extension of the file containing the Image
        """
        self.location_path = location_path
        self.name = name
        self.extension = extension
