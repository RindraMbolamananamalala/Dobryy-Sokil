# -*- coding: utf-8 -*-

"""
word_finder_AS_intf.py: The python file dedicated to the Abstract Base Class NLP Application Service
for any finding process related to words
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

from abc import ABC, abstractmethod


class WordFinderASIntf(ABC):
    @abstractmethod
    def find_word_close_neighbors(self, word: str) -> set():
        """
        Finding the set of words that can be considered, with "high" confidence, as neighbors of a given "correct" word.
        :param word: The word whose neighbors are to be found
        :return: The list of words that are the neighbors, with "high" confidence, of the word given within the parameter
        """
        return

    @abstractmethod
    def find_word_likely_neighbors(self, word: str) -> set():
        """
        Finding the set of words that can be considered, with "relatively high" confidence, as neighbors of a given
        "correct" word.
        :param word: The word whose neighbors are to be found
        :return: The list of words that are the neighbors, with "relatively high" confidence, of the word given within
        the parameter
        """
        return
