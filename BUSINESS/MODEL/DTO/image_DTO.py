# -*- coding: utf-8 -*-

"""
image_DTO.py: The python file dedicated to the "Model:DataTransferObject:Image" part of the MVC pattern implemented within
the "BUSINESS" layer of the Project, and at the same time one of the Project's DTOs
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

from typing import Optional

from BUSINESS.MODEL.DTO.dobryy_sokil_DTO import DobryySokilDTO
from BUSINESS.MODEL.DOMAIN_OBJECTS.word import Word


class ImageDTO(DobryySokilDTO):

    def set_location_path(self, location_path: Optional[str]):
        """

        :param location_path: The path of the directory where the file containing the Image is located
        :return: None
        """
        self.location_path = location_path

    def get_location_path(self) -> Optional[str]:
        """

        :return: The path of the directory where the file containing the Image is located
        """
        return self.location_path

    def set_name(self, name: Optional[str]):
        """

        :param name: The filename of the file containing the Image
        :return: None
        """
        self.name = name

    def get_name(self) -> Optional[str]:
        """

        :return: The filename of the file containing the Image
        """
        return self.name

    def set_extension(self, extension: Optional[str]):
        """

        :param extension: The extension of the file containing the Image
        :return:
        """
        self.extension = extension

    def get_extension(self) -> Optional[str]:
        """

        :return: The extension of the file containing the Image
        """
        return self.extension

    def set_labels_of_visual_elements_contained(self, labels_of_visual_elements_contained: Optional[list(Word)]):
        """

        :param labels_of_visual_elements_contained: The set of labels of the visual elements contained inside the Image
        :return: None
        """
        self.labels_of_visual_elements_contained = labels_of_visual_elements_contained

    def get_labels_of_visual_elements_contained(self) -> Optional[list(Word)]:
        """

        :return: The set of labels of the visual elements contained inside the Image
        """
        return self.labels_of_visual_elements_contained

    def get_absolute_path(self) -> Optional[str]:
        """

        :return: The absolute path of the file containing the Image
        """
        return self.get_location_path().replace("/", "\\") \
               + "\\" \
               + self.get_name() \
               + "." \
               + self.get_extension()

    def __init__(self
                 , location_path: Optional[str]
                 , name: Optional[str]
                 , extension: Optional[str]):
        """

        :param location_path: The path of the directory where the file containing the Image is located
        :param name: The filename of the file containing the Image
        :param extension: The extension of the file containing the Image
        """
        self.location_path = location_path
        self.name = name
        self.extension = extension
