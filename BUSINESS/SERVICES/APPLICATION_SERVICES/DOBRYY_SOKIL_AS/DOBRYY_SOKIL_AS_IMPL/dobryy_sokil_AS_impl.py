# -*- coding: utf-8 -*-

"""
dobryy_sokil_AS_impl.py: The python file dedicated to the Implementation Class of the Dobryy Sokil Application
Service part dedicated to any implementation of action obtained with the Modeling process of a Real World "smart"
Sokil (The Ukrainian world for Falcon)
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

from UTILS.image_utils import get_all_images_within_a_folder

from CONFIGURATIONS.logger import LOGGER

from BUSINESS.CONSTRAINTS.CONVERTER.CONVERTER_IMPL.image_converter import image_file_paths_to_image_domain_objects

from BUSINESS.SERVICES.APPLICATION_SERVICES.DOBRYY_SOKIL_AS.DOBRYY_SOKIL_AS_INTF.dobryy_sokil_AS_intf import \
    DobryySokilASIntf
from BUSINESS.SERVICES.APPLICATION_SERVICES.AI_AS.NLP_AS.NLP_AS_INTF.word_matcher_AS_intf import WordMatcherASIntf
from BUSINESS.SERVICES.APPLICATION_SERVICES.AI_AS.NLP_AS.NLP_AS_IMPL.word_matcher_AS_impl import WordMatcherASImpl
from BUSINESS.SERVICES.APPLICATION_SERVICES.AI_AS.ML_AS.ML_AS_INTF.image_classifier_AS_intf import ImageClassifierASIntf
from BUSINESS.SERVICES.APPLICATION_SERVICES.AI_AS.ML_AS.ML_AS_IMPL.image_classifier_AS_impl import ImageClassifierASImpl


class DobryySokilASImpl(DobryySokilASIntf):

    def set_word_matcher_as(self, word_matcher_as: WordMatcherASIntf):
        """

        :param word_matcher_as: The NLP.Word_Matcher Application Service to be used throughout the entire current
        Application Service.
        :return: None
        """
        self.word_matcher_as = word_matcher_as

    def get_word_matcher_as(self):
        """

        :return:  The NLP.Word_Matcher Application Service used throughout the entire current
        Application Service
        """
        return self.word_matcher_as

    def set_image_classifier_as(self, image_classifier_as: ImageClassifierASIntf):
        self.image_classifier_as = image_classifier_as

    def get_image_classifier_as(self):
        return self.image_classifier_as

    def hunt(self, object_to_search: str, root_folder_path: str):
        """
        The Dobryy Sokil's M1 Level model representation of an actual hunt of a target prey in a given perimeter
        in the Real World (M0) Level.

        :param object_to_search: the "label" of the object to find, the current Model (M1) Level equivalent of the Real
        World Level (M0) Sokil's prey
        :param root_folder_path: root_folder_path: the "Root" folder's path for the search, the current Model (M1) Level
        equivalent of the Real World Lever (M0) perimeter of search
        :return: The list of Image Objects within the Root Folder that are related to the Object to Search, the current
        Model (M1) Level equivalent of the Real World Level (M0) potential grabbed prey of the Sokil.
        """
        try:
            if object_to_search and root_folder_path:
                # Valid arguments were provided

                # Initializing the lists of results
                list_of_images_found = []

                # Retrieving all the Images contained within the Root Folder
                images_to_classify_paths = get_all_images_within_a_folder(root_folder_path)
                images_to_classify = image_file_paths_to_image_domain_objects(images_to_classify_paths)

                # Predicting the possible labels of each Image contained within the Root Folder
                root_folder_classified_images = self.get_image_classifier_as().predict(images_to_classify)

                # Filtering the previous Classified Image in function of their relation with the Object to search
                for root_folder_classified_image in root_folder_classified_images:
                    for image_possible_label in root_folder_classified_image.get_predicted_labels():
                        # The relation between the Object to search and the current Image is determined by a NLP
                        # Matching process
                        if self.get_word_matcher_as().are_two_words_related(object_to_search, image_possible_label):
                            list_of_images_found.append(root_folder_classified_image)
                            break
                if len(list_of_images_found) > 0:
                    # A successful Hunt
                    LOGGER.info(
                        "Result of the Hunt related to the Object to search \"" + object_to_search + "\""
                        + " within the Root Folder \"" + root_folder_path + "\"" + ": "
                        + str(list_of_images_found)
                    )
                    return list_of_images_found
                # The Hunt wasn't successful
                LOGGER.info(
                    "No element related to the Object to search \"" + object_to_search
                    + "\"" + "was found within the Root Folder \"" + root_folder_path + "\""
                )
                return []
            else:
                # At least one of the required Arguments was Empty or None
                LOGGER.error("At least one of the required Arguments was Empty of None")
                raise TypeError
        except Exception as exception:
            # At least one error has occurred, therefore, stop the Hunt process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Hunt. "
            )
            raise

    def __init__(self):
        # Preparation of all the other Application Services to be used by the current Application Service
        self.set_word_matcher_as(WordMatcherASImpl())
        self.set_image_classifier_as(ImageClassifierASImpl())
