# -*- coding: utf-8 -*-

"""
test_predict.py: The python file dedicated to the Unit Testing of the
BUSINESS.SERVICES.APPLICATION_SERVICES.AI_AS.ML_AS.ML_AS_IMPL.image_classifier_AS_impl.ImageClassifierASImpl.predict()"
function
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

import os
import unittest

from BUSINESS.MODEL.DOMAIN_OBJECTS.image import Image
from BUSINESS.MODEL.DTO.classified_image_DTO import ClassifiedImageDTO
from BUSINESS.SERVICES.APPLICATION_SERVICES.AI_AS.ML_AS.ML_AS_IMPL.image_classifier_AS_impl import ImageClassifierASImpl


class TestPredict(unittest.TestCase):

    def test_predict(self):
        """
        GIVEN a not yet classified List of Images are provided
        WHEN the predict() method of the ImageClassifierASImpl is called, with the previous List as its parameter,
        THEN a valid list of Images, this time with their relative labels predicted, must be returned
        """

        # Preparing the Image Classifier instance for the series of tests
        image_classifier = ImageClassifierASImpl()

        # If None or Empty list of Images provided, an empty list must be returned
        assert image_classifier.predict(None) == [] and image_classifier.predict([]) == []

        # If a non-valid Image provided, the predict() function must raise an Exception
        self.assertRaises(Exception, image_classifier.predict, [""])
        self.assertRaises(Exception, image_classifier.predict, [" "])
        self.assertRaises(Exception, image_classifier.predict, ["aaaa99993222222"])
        self.assertRaises(Exception, image_classifier.predict, ["aaaa99993222222.JPG"])

        """
        Real Time use simulations
        """
        # Getting the path leading to the Image Resources especially dedicated to the tests related to the Image
        # Classifier AS
        test_resources_folder_path = os.getcwd().split("Добрый_Сокол")[0] \
                                     + "Добрый_Сокол" \
                                     + "/TESTS/UNIT_TESTS/RESOURCES"
        test_image_resources = test_resources_folder_path.replace("\\", "/") \
                               + "/IMAGE"

        # Preparing the data for the Real Time use simulation
        real_time_use_test_data = [
            # ([<images_to_predict>, <expected_predictions>])

            # Image containing a Soccer Ball
            ([Image(test_image_resources, "Ball", "JPG")],
             [ClassifiedImageDTO(test_image_resources, "Ball", "JPG", ["soccer_ball"])]),

            # Image containing a Spider
            ([Image(test_image_resources, "Spider", "JPG")],
             [ClassifiedImageDTO(test_image_resources, "Spider", "JPG", ["tarantula"])]),

            # Image containing a Wolf
            ([Image(test_image_resources, "Wolf", "JPG")],
             [ClassifiedImageDTO(test_image_resources, "Wolf", "JPG", ["timber_wolf"])]),

            # Image of a Fruits Bowl
            ([Image(test_image_resources, "FruitsBowl", "JPG")],
             [ClassifiedImageDTO(test_image_resources, "FruitsBowl", "JPG", ["lemon", "orange", "banana"])])
        ]

        # An image containing  only a soccer ball contains a "soccer ball", a must not contain a "glue"
        assert image_classifier.predict(real_time_use_test_data[0][0])[0] \
            .get_predicted_labels().__contains__("soccer_ball")
        assert not image_classifier.predict(real_time_use_test_data[0][0])[0] \
            .get_predicted_labels().__contains__("glue")
        assert image_classifier.predict(real_time_use_test_data[0][0]) == real_time_use_test_data[0][1]

        # An image containing only a Tarantula contains a "Tarantula", a must not contain a crab, a fish or a dog
        assert image_classifier.predict(real_time_use_test_data[1][0])[0] \
            .get_predicted_labels().__contains__("tarantula")
        assert not image_classifier.predict(real_time_use_test_data[1][0])[0] \
            .get_predicted_labels().__contains__("crab")
        assert not image_classifier.predict(real_time_use_test_data[1][0])[0] \
            .get_predicted_labels().__contains__("fish")
        assert not image_classifier.predict(real_time_use_test_data[1][0])[0] \
            .get_predicted_labels().__contains__("dog")
        assert image_classifier.predict(real_time_use_test_data[1][0]) == real_time_use_test_data[1][1]

        # An image containing only a "Timber Wolf" contains a "timber wolf", a must not contain a fish or a television
        assert image_classifier.predict(real_time_use_test_data[2][0])[0] \
            .get_predicted_labels().__contains__("timber_wolf")
        assert not image_classifier.predict(real_time_use_test_data[2][0])[0] \
            .get_predicted_labels().__contains__("fish")
        assert not image_classifier.predict(real_time_use_test_data[2][0])[0] \
            .get_predicted_labels().__contains__("television")
        assert image_classifier.predict(real_time_use_test_data[2][0]) == real_time_use_test_data[2][1]

        # An image containing a "Fruits Bowl" contains a "Banana" and an "Orange", and must not contain
        # a hammer or a penguin
        assert image_classifier.predict(real_time_use_test_data[3][0])[0] \
            .get_predicted_labels().__contains__("banana")
        assert image_classifier.predict(real_time_use_test_data[3][0])[0] \
            .get_predicted_labels().__contains__("orange")
        assert not image_classifier.predict(real_time_use_test_data[3][0])[0] \
            .get_predicted_labels().__contains__("hammer")
        assert not image_classifier.predict(real_time_use_test_data[3][0])[0] \
            .get_predicted_labels().__contains__("penguin")
        assert image_classifier.predict(real_time_use_test_data[3][0]) == real_time_use_test_data[3][1]
