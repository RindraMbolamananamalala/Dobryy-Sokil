# -*- coding: utf-8 -*-

"""
classified_image_DTO.py: The python file dedicated to the "Model:DataTransferObject:ClassifiedImage" part of the MVC
pattern implemented within the "BUSINESS" layer of the Project, and at the same time one of the Project's DTOs
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"


from BUSINESS.MODEL.DTO.image_DTO import ImageDTO


class ClassifiedImageDTO(ImageDTO):

    def set_predicted_labels(self, predicted_labels: list):
        """

        :param predicted_labels: The list of labels predicted for the Image
        :return:
        """
        self.predicted_labels = predicted_labels

    def get_predicted_labels(self) -> list:
        """

        :return: The list of labels predicted for the Image
        """
        return self.predicted_labels

    def __init__(self, *args):
        """

        :param location_path: The path of the directory where the file containing the Image is located
        :param name: The filename of the file containing the Image
        :param extension: The extension of the file containing the Image
        :param predicted_labels: The list of labels predicted for the Image
        """
        if len(args) != 4:
            # To be managed according to the Superclass definition
            super().__init__(*args)
            self.predicted_labels = list()
        elif len(args) == 4:
            # the list of predicted labels was provided
            super().__init__(
                # location_path
                args[0]
                # name
                , args[1]
                # extension
                , args[2]
            )
            # predicted_labels
            self.set_predicted_labels(args[3])

