# -*- coding: utf-8 -*-

"""
word.py: The python file dedicated to the "Model:Word" part of the MVC pattern implemented within
the "BUSINESS" layer of the Project, and at the same time one of the Project's DOs
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

from BUSINESS.MODEL.DOMAIN_OBJECTS.dobryy_sokil_DO import DobryySokilDO
from BUSINESS.MODEL.DOMAIN_OBJECTS.word import Word


class Word(DobryySokilDO):
    def set_content(self, content: str):
        self.content = content

    def get_content(self) -> str:
        return self.content

    def set_synonyms(self, synonyms: [Word]):
        self.synonyms = synonyms

    def get_synonyms(self) -> [Word]:
        return self.synonyms

    def set_homonyms(self, homonyms: [Word]):
        self.homonyms = homonyms

    def get_homonyms(self) -> [Word]:
        return self.homonyms

    def set_associated_words(self, associated_words: [Word]):
        self.associated_words = associated_words

    def get_associated_words(self) -> [Word]:
        return self.associated_words

    def __init__(self):
        self.set_content(None)
        self.set_synonyms(None)
        self.set_homonyms(None)
        self.set_associated_words(None)

    def __init__(self, content):
        self.set_content(content)
