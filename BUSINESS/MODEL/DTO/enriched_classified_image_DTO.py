# -*- coding: utf-8 -*-

"""
enriched_classified_image_DTO.py: The python file dedicated to the "Model:DataTransferObject:EnrichedClassifiedImage"
part of the MVC pattern, a particular subclass of the "Model:DataTransferObject:ClassifiedImage", implemented within
the "BUSINESS" layer of the Project, and at the same time one of the Project's DTOs
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

from BUSINESS.MODEL.DTO.classified_image_DTO import ClassifiedImageDTO


class EnrichedClassifiedImageDTO(ClassifiedImageDTO):

    def set_labels_neighbors(self, labels_neighbors: set):
        """

        :param labels_neighbors: The words considered as potential neighbors of the possible labels of the already
        classified Image
        :return: None
        """
        self.labels_neighbors = labels_neighbors

    def get_labels_neighbors(self) -> set:
        """

        :return: The words considered as potential neighbors of the possible labels of the already classified Image
        """
        return self.labels_neighbors

    def __init__(self, *args):
        super().__init__(*args)
        # The set for the Neighbors of the Image's possible labels set to an Empty one at the start, but it has to be
        # fed later in order to properly exploit this particular DTO
        self.labels_neighbors = set()

