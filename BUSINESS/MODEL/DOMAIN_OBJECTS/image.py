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
from BUSINESS.MODEL.DOMAIN_OBJECTS.word import Word


class Image(DobryySokilDO):

    def set_location_path(self, location_path: str):
        """

        :param location_path: The path of the directory where the file containing the Image is located
        :return: None
        """
        self.location_path = location_path

    def get_location_path(self) -> str:
        """

        :return: The path of the directory where the file containing the Image is located
        """
        return self.location_path

    def set_name(self, name: str):
        """

        :param name: The filename of the file containing the Image
        :return: None
        """
        self.name = name

    def get_name(self) -> str:
        """

        :return: The filename of the file containing the Image
        """
        return self.name

    def set_extension(self, extension: str):
        """

        :param extension: The extension of the file containing the Image
        :return:
        """
        self.extension = extension

    def get_extension(self) -> str:
        """

        :return: The extension of the file containing the Image
        """
        return self.extension

    def set_labels_of_visual_elements_contained(self, labels_of_visual_elements_contained: [Word]):
        """

        :param labels_of_visual_elements_contained: The set of labels of the visual elements contained inside the Image
        :return: None
        """
        self.labels_of_visual_elements_contained = labels_of_visual_elements_contained

    def get_labels_of_visual_elements_contained(self) -> [Word]:
        """

        :return: The set of labels of the visual elements contained inside the Image
        """
        return self.labels_of_visual_elements_contained

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

    def __init__(self):
        # All the properties set to None at the start
        self.location_path = None
        self.name = None
        self.extension = None