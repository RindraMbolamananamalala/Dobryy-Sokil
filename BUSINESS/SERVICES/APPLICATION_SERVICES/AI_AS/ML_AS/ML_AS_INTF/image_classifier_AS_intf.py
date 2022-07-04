# -*- coding: utf-8 -*-

"""
image_classifier_AS_intf.py: The python file dedicated to the Abstract Base Class of the Deep Learning Application
Service part dedicated to the prediction of the probable Labels of Images
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

from abc import ABC, abstractmethod

from BUSINESS.MODEL.DOMAIN_OBJECTS.image import Image
from BUSINESS.MODEL.DTO.classified_image_DTO import ClassifiedImageDTO


class ImageClassifierASIntf(ABC):
    @abstractmethod
    def predict(self, images: [Image]) -> [ClassifiedImageDTO]:
        """
        Classifying (predicting their probable labels) a list of Images provided in parameters.

        :param images: The list of Images to be classified
        :return: A list of Image DTOs with their "predicted labels" list fed by labels predicted by a
        dedicated DL Model from the list of Images provided within the parameters.
        """
        return
