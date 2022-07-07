# -*- coding: utf-8 -*-

"""
test_are_two_words_related.py: The python file dedicated to Unit Testing of the
BUSINESS.SERVICES.APPLICATION_SERVICES.AI_AS.NLP_AS.NLP_AS_IMPL.word_matcher_AS_impl.WordMatcherASImpl
.are_two_words_related()"
function
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

import unittest
import warnings

from BUSINESS.SERVICES.APPLICATION_SERVICES.AI_AS.NLP_AS.NLP_AS_IMPL.word_matcher_AS_impl import WordMatcherASImpl


def ignore_resource_warnings(test_func):
    """
    Not showing as part of the Logs the Warning message related to the "ResourceWarning"
    """

    def do_test(self, *args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", ResourceWarning)
            test_func(self, *args, **kwargs)

    return do_test


class TestAreTwoWordsRelated(unittest.TestCase):
    """
    Do not show the resource warning messages related to the specific reading processes managed by TextBlob
    """

    @ignore_resource_warnings
    def test_are_two_words_related(self):
        """
        GIVEN two words w1 and w2 provided as parameters and we want to know if they're related or not w.r.t their
        meanings,
        WHEN the are_two_words_related(w1, w2) method of the WordMatcherASImpl is called, with the previous words within
        its parameters,
        THEN the status of the "matching" between them, w.r.t their meanings, must be correctly returned
        """

        # Preparing the Word Matcher AS for the tests
        word_matcher_as = WordMatcherASImpl()

        # Preparing the Data for the tests
        data_for_the_tests = [
            # (w1, w2, matching_status_expected)

            # The management of "None"  and blank strings provided within the parameters must be respected
            (None, None, None)
            , (None, "Word", None)
            , ("Word", None, None)
            , ("", "", None)
            , ("", "Word", None)
            , ("Word", "", None)

            # Simulations of actual uses of the matcher

            # "Timber Wolf" and "Grey Wolf" are related
            , ("Timber wolf", "grey Wolf", True)
            , ("Timber_wolf", "Grey Wolf", True)
            , ("Timber_Wolf", "Grey_Wolf", True)
            , ("Timber_Wolf", "Gray_Wolf", True)

            # "Plane" and "Airplane" are related
            , ("Plane", "Airplane", True)

            # "Hammer" and "Pan" are not related
            , ("Hammer", "Pan", False)

            # "Car" and "Mask" are not related
            , ("Car", "Mask", False)

            # "Banana" and "Caterpillar" are not related
            , ("Banana", "Caterpillar", False)

        ]

        # Actual tests
        for data in data_for_the_tests:
            assert word_matcher_as.are_two_words_related(data[0], data[1]) == data[2]
