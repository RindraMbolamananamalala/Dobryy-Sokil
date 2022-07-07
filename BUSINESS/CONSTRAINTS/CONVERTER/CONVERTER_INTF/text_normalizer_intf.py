# -*- coding: utf-8 -*-

"""
text_normalizer_intf.py: The python file dedicated to the Abstract Base Class for the text normalization process
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

from abc import ABC, abstractmethod


class TextNormalizerIntf(ABC):

    @abstractmethod
    def normalize(self, text_to_normalize: str) -> str:
        """
        Transforming a text into one canonical form, this latter chosen according to the specific needs
        within the Dobryy Sokil Project.

        :param text_to_normalize: The text to normalize
        :return: The normalized version of the text put in parameters
        """
        return

    @abstractmethod
    def normalize_for_nlp(self, text_to_normalize: str) -> str:
        """
        Firstly, transforming a text into one canonical form, this latter chosen according to the specific needs
        within the Dobryy Sokil Project.
        Secondly, transforming the previous normalized text to another version according to the specific needs for
        NLP.

        :param text_to_normalize: The text to normalize
        :return: The NLP-normalized version of the text put in parameters
        """
        return
        
        
