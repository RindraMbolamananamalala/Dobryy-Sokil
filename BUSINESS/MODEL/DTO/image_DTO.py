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

from CONFIGURATIONS.logger import LOGGER
from BUSINESS.MODEL.DTO.dobryy_sokil_DTO import DobryySokilDTO


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

    def set_labels_of_visual_elements_contained(self, labels_of_visual_elements_contained: Optional[list]):
        """

        :param labels_of_visual_elements_contained: The set of labels of the visual elements contained inside the Image
        :return: None
        """
        self.labels_of_visual_elements_contained = labels_of_visual_elements_contained

    def get_labels_of_visual_elements_contained(self) -> Optional[list]:
        """

        :return: The set of labels of the visual elements contained inside the Image
        """
        return self.labels_of_visual_elements_contained

    def get_absolute_path(self) -> Optional[str]:
        """

        :return: The absolute path of the file containing the Image
        """
        if self.get_location_path() and self.get_name() and self.get_extension():
            # Only a valid Image DTO can have a valid absolute path
            return self.get_location_path().replace("\\", "/") \
                   + "/" \
                   + self.get_name() \
                   + "." \
                   + self.get_extension()
        # Not a valid Image DTO, therefore, return a blank string
        return ""

    def __init__(self, *args):
        """

        :param location_path: The path of the directory where the file containing the Image is located
        :param name: The filename of the file containing the Image
        :param extension: The extension of the file containing the Image
        """
        if len(args) == 0:
            # No argument was given, therefore, all the properties set to None at the start
            self.location_path = None
            self.name = None
            self.extension = None
        elif len(args) == 3:
            # The Location path, Name and the File Extension of the Image DTO were given
            self.location_path = args[0]
            self.name = args[1]
            self.extension = args[2]
        else:
            # Invalid numbers of arguments
            msg_error = "Invalid numbers of arguments given for the instantiation of an Image DTO"
            LOGGER.error(msg_error)
            exception = TypeError(msg_error)
            raise exception
