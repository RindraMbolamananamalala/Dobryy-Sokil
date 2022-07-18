# -*- coding: utf-8 -*-

"""
test_find_word_close_neighbors.py: The python file dedicated to Unit Testing of the
BUSINESS.SERVICES.APPLICATION_SERVICES.AI_AS.NLP_AS.NLP_AS_IMPL.word_finder_AS_impl.WordFinderASImpl.find_word_close_neighbors()"
function
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

import unittest

from BUSINESS.SERVICES.APPLICATION_SERVICES.AI_AS.NLP_AS.NLP_AS_IMPL.word_finder_AS_impl import WordFinderASImpl


class TestFindWordCloseNeighbors(unittest.TestCase):
    def test_find_word_close_neighbors(self):
        """
        GIVEN a correct word provided within the parameter
        WHEN the find_word_close_neighbors() method of the WordFinderASImpl is called, with the previous word within
        its parameters,
        THEN a set of the words considered as being its close neighbors must be returned
        """

        # Preparing the WordFinderAS instance for the test
        word_finder_for_the_test = WordFinderASImpl()

        """Actual Testing part"""

        # If a "None" word is provided, it should return an blank set
        assert word_finder_for_the_test.find_word_close_neighbors(None) is not None \
               and word_finder_for_the_test.find_word_close_neighbors(None) == set()

        # If a "Blank" word is provided, it should return an blank set
        assert word_finder_for_the_test.find_word_close_neighbors("") is not None \
               and word_finder_for_the_test.find_word_close_neighbors("") == set()

        # Simulating a real time use of the service for the close neighbors finding process with the word "plane"
        plane_neighbors = word_finder_for_the_test.find_word_likely_neighbors("plane")
        assert plane_neighbors is not None \
               and len(plane_neighbors) > 1
        # The word "aeroplane" is a close neighbor of the word "plane"
        assert plane_neighbors.__contains__("aeroplane")
        # The word "airplane" is a close neighbor of the word "plane"
        assert plane_neighbors.__contains__("airplane")
        # The word "cockroach" is not a close neighbor of the word "plane"
        assert not plane_neighbors.__contains__("cockroach")

        # Simulating a real time use of the service for the close neighbors finding process with the word "hamburger"
        hamburger_neighbors = word_finder_for_the_test.find_word_close_neighbors("hamburger")
        assert hamburger_neighbors is not None \
               and len(hamburger_neighbors) > 1
        # The word "burger" is a close neighbor of the word "hamburger"
        assert hamburger_neighbors.__contains__("burger")
        # The word "ground beef" is a close neighbor of the word "hamburger"
        assert hamburger_neighbors.__contains__("ground_beef")
        # The word "beefburger" is a close neighbor of the word "hamburger"
        assert hamburger_neighbors.__contains__("beefburger")
        # The word "sandwich" is not a close neighbor of the word "hamburger"
        assert not hamburger_neighbors.__contains__("sandwich")
        # The word "president" is not a close neighbor of the word "hamburger"
        assert not hamburger_neighbors.__contains__("president")
