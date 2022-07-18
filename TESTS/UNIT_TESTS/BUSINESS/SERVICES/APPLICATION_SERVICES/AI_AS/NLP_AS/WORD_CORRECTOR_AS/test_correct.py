# -*- coding: utf-8 -*-

"""
test_correct.py: The python file dedicated to Unit Testing of the
BUSINESS.SERVICES.APPLICATION_SERVICES.AI_AS.NLP_AS.NLP_AS_IMPL.word_corrector_AS_impl.WordCorrectorASImpl.correct()"
function
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

import unittest
import warnings

from BUSINESS.SERVICES.APPLICATION_SERVICES.AI_AS.NLP_AS.NLP_AS_IMPL.word_corrector_AS_impl import WordCorrectorASImpl


def ignore_resource_warnings(test_func):
    """
    Not showing as part of the Logs the Warning message related to the "ResourceWarning"
    """
    def do_test(self, *args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", ResourceWarning)
            test_func(self, *args, **kwargs)

    return do_test


class TestCorrect(unittest.TestCase):

    """
    Do not show the resource warning messages related to the specific reading processes managed by TextBlob
    """
    @ignore_resource_warnings
    def test_correct(self):
        """
        GIVEN a word not yet correct word (w.r.t its Spellings)
        WHEN the correct() method of the WordCorrectorASImpl is called, with the previous word as its parameter,
        THEN a correct word (w.r.t its Spellings) must be returned
        """

        """
        Preparing the Word Corrector instance for the test
        """
        word_corrector_for_the_test = WordCorrectorASImpl()

        """
        Preparing the Tests Data
        """
        tests_data = [
            # Structure of the Couple :
            #   (<Word Not yet correct>, <Corrected version expected>)

            # Verifying that the fact of entering no word is correctly managed
            (None, "")
            , ("", "")

            # Simulating a real use of the Spelling correction service
            , ("humen", "human")
            , ("whitle", "while")
            , ("dogg", "dog")
            , ("liiiionnnnnn", "lion")
            , ("a", "a")
            , ("aa", "a")
            , ("aaa", "a")
            , ("correspondance", "correspondence")
            , ("Matrixe", "Matrix")
            , ("Haeven", "Even")
        ]

        # Launching the actual testing processes
        for tests_data_couple in tests_data:
            assert word_corrector_for_the_test.correct(tests_data_couple[0]) == tests_data_couple[1]

