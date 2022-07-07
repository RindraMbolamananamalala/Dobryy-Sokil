# -*- coding: utf-8 -*-


"""
word.py: The python file dedicated to the "Model:Word" part of the MVC pattern implemented within
the "BUSINESS" layer of the Project, and at the same time one of the Project's DOs
"""

# In order to enable the use of the current class as already possible types for its own properties
from __future__ import annotations

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

from BUSINESS.MODEL.DOMAIN_OBJECTS.dobryy_sokil_DO import DobryySokilDO


class Word(DobryySokilDO):
    def set_content(self, content: str):
        """

        :param content: The actual word contained in this dedicated object
        :return:
        """
        self.content = content

    def get_content(self) -> str:
        """

        :return: The actual word contained in this dedicated object
        """
        return self.content

    def set_synonyms(self, synonyms: set):
        """

        :param synonyms: The set of synonyms of the word corresponding to this current dedicated object
        :return: None
        """
        self.synonyms = synonyms

    def get_synonyms(self) -> set:
        """

        :return: The set of synonyms of the word corresponding to this current dedicated object
        """
        return self.synonyms

    def set_homonyms(self, homonyms: set):
        """

        :param homonyms: The set of homonyms of the word corresponding to this current dedicated object
        :return:
        """
        self.homonyms = homonyms

    def get_homonyms(self) -> set:
        """

        :return: The set of homonyms of the word corresponding to this current dedicated object
        """
        return self.homonyms

    def set_associated_words(self, associated_words: set):
        """

        :param associated_words:  The set of associated words of the word corresponding to this current dedicated object
        :return: None
        """
        self.associated_words = associated_words

    def get_associated_words(self) -> set:
        """

        :return: The set of associated words of the word corresponding to this current dedicated object
        """
        return self.associated_words

    def __init__(self, *args):
        """

        :param content: The actual word contained in this dedicated object
        """
        if len(args) == 0:
            # No argument was provided, so, at the start, just set all the properties to Empty sets
            self.set_content(set())
            self.set_synonyms(set())
            self.set_homonyms(set())
            self.set_associated_words(set())
        if len(args) == 1:
            # The Word's content was provided
            self.set_content(args[0])


