# -*- coding: utf-8 -*-

"""
word_matcher_AS_intf.py: The python file dedicated to the Abstract Base Class of the NLP Application Service for
any need of word matching
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

from abc import ABC, abstractmethod


class WordMatcherASIntf(ABC):
    @abstractmethod
    def are_two_words_related(self, word_1: str, word_2: str):
        """

        :param word_1: The first Word for the Matching process
        :param word_2: The second Word for the Matching process
        :return: TRUE if the two words are related w.r.t their meanings, FALSE otherwise.
        """
        return
