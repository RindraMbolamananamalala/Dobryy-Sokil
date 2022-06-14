# -*- coding: utf-8 -*-

"""
word_corrector_AS_intf.py: The python file dedicated to the Abstract Base Class of NLP Application Service for
the spellings correction of word
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

from abc import ABC, abstractmethod


class WordCorrectorASIntf(ABC):
    @abstractmethod
    def correct(self, word: str):
        """
        Correcting the Spelling of a word inserted within the parameter.
        :param word: The word to be corrected (w.r.t its Spelling)
        :return: The corrected version (w.r.t its Spelling) of the word inserted within the parameter
        """
        return

