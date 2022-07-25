# -*- coding: utf-8 -*-

"""
test_hunt.py: The python file dedicated to Unit Testing of the
BUSINESS.SERVICES.APPLICATION_SERVICES.DOBRYY_SOKIL_AS.DOBRYY_SOKIL_AS_IMPL.dobryy_sokil_AS_impl.DobryySokilASImpl
.hunt()" function
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

import os
import unittest
import warnings

from BUSINESS.SERVICES.APPLICATION_SERVICES.DOBRYY_SOKIL_AS.DOBRYY_SOKIL_AS_IMPL.dobryy_sokil_AS_impl import \
    DobryySokilASImpl


def ignore_resource_warnings(test_func):
    """
    Not showing as part of the Logs the Warning message related to the "ResourceWarning"
    """

    def do_test(self, *args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", ResourceWarning)
            test_func(self, *args, **kwargs)

    return do_test


class TestHunt(unittest.TestCase):
    """
    Do not show the resource warning messages related to the specific reading processes managed by TextBlob
    """

    @ignore_resource_warnings
    def test_hunt(self):
        """
        GIVEN a valid label of Object to be found and a valid path corresponding to the ROOT folder of the search
        process,
        WHEN the hunt(object_label, root_folder_path) method of the WordMatcherASImpl is called, with the previous
        elements in parameters
        THEN a correct list of Image
        """

        # preparing the Dobryy Sokil AS for the tests
        dobryy_sokil_as_for_the_test = DobryySokilASImpl()

        """ 
        Tests related to the validity of the Arguments provided to the hunt() function
        """
        # If at least one of the arguments provided is None or Empty, a TypeError Exception must be raised
        self.assertRaises(TypeError, dobryy_sokil_as_for_the_test, None, None)
        self.assertRaises(TypeError, dobryy_sokil_as_for_the_test, None, "C:/")
        self.assertRaises(TypeError, dobryy_sokil_as_for_the_test, "Object", None)
        self.assertRaises(TypeError, dobryy_sokil_as_for_the_test, "", "")
        self.assertRaises(TypeError, dobryy_sokil_as_for_the_test, "", "C:/")
        self.assertRaises(TypeError, dobryy_sokil_as_for_the_test, "Object", "")
        self.assertRaises(TypeError, dobryy_sokil_as_for_the_test, None, None)
        self.assertRaises(TypeError, dobryy_sokil_as_for_the_test, None, "C:/")
        self.assertRaises(TypeError, dobryy_sokil_as_for_the_test, "", None)
        self.assertRaises(TypeError, dobryy_sokil_as_for_the_test, None, "")

        """
        Simulations of real time uses of the Hunt() function
        """
        # First, let's get the path leading to the Image Resources especially dedicated to any need of Image
        # classification during tests
        test_resources_folder_path = os.getcwd().split("Добрый_Сокол")[0] \
                                     + "Добрый_Сокол" \
                                     + "/TESTS/UNIT_TESTS/RESOURCES"
        test_image_resources = test_resources_folder_path.replace("\\", "/") \
                               + "/IMAGE"

        # The Folder of Image Resources contains one image containing a "Timber Wolf" named "Wolf.jpg"
        assert len(dobryy_sokil_as_for_the_test.hunt("Timber Wolf", test_image_resources)) == 1
        assert len(dobryy_sokil_as_for_the_test.hunt("Gray Wolf", test_image_resources)) == 1
        assert dobryy_sokil_as_for_the_test.hunt("Timber Wolf", test_image_resources)[0].get_name() == "Wolf"
        assert dobryy_sokil_as_for_the_test.hunt("Timber Wolf", test_image_resources)[0].get_extension() == "JPG"
        assert dobryy_sokil_as_for_the_test.hunt("Timber Wolf", test_image_resources)[0].get_absolute_path() \
               == test_image_resources + "/Wolf.JPG"

        # The Folder of "Not_a_Disk/Not_a_Folder/Not_an_Image/" (fictional) doesn't contain any image containing a
        # "Timber Wolf"
        assert len(dobryy_sokil_as_for_the_test.hunt("Timber Wolf", "Not_a_Disk/Not_a_Folder/Not_an_Image/")) == 0

        # The Folder of Image Resources contains one image containing an "Orange" named "FruitsBowl.jpg"
        assert len(dobryy_sokil_as_for_the_test.hunt("Orange", test_image_resources)) == 1
        assert dobryy_sokil_as_for_the_test.hunt("Orange", test_image_resources)[0].get_name() == "FruitsBowl"
        assert dobryy_sokil_as_for_the_test.hunt("Orange", test_image_resources)[0].get_extension() == "jpg"
        assert dobryy_sokil_as_for_the_test.hunt("Orange", test_image_resources)[0].get_absolute_path() \
               == test_image_resources + "/FruitsBowl.jpg"

        # The Folder of Image Resources contains two images containing a "Soccer ball" named respectively
        # "Ball.jpg" and "Football.jpg"
        assert len(dobryy_sokil_as_for_the_test.hunt("Soccer ball", test_image_resources)) == 2
        assert (dobryy_sokil_as_for_the_test.hunt("Soccer ball", test_image_resources)[0].get_name() == "Ball") \
               or \
               (dobryy_sokil_as_for_the_test.hunt("Soccer ball", test_image_resources)[1].get_name() == "Ball")
        assert (dobryy_sokil_as_for_the_test.hunt("Soccer ball", test_image_resources)[0].get_name() == "Football") \
               or \
               (dobryy_sokil_as_for_the_test.hunt("Soccer ball", test_image_resources)[1].get_name() == "Football")

        # The Folder of Image Resources doesn't contain any Image containing a "Lake"
        assert len(dobryy_sokil_as_for_the_test.hunt("Lake", test_image_resources)) == 0

        # The Folder of Image Resources doesn't contain any Image containing a "Rubber"
        assert len(dobryy_sokil_as_for_the_test.hunt("Rubber", test_image_resources)) == 0

        # The Folder of Image Resources doesn't contain any Image containing a "Javelin"
        assert len(dobryy_sokil_as_for_the_test.hunt("Javelin", test_image_resources)) == 0
