# -*- coding: utf-8 -*-

"""
word_matcher_AS_impl.py: The python file dedicated to the Implementation Class of the NLP Application Service for
any need of word matching
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

from CONFIGURATIONS.logger import LOGGER

from BUSINESS.MODEL.DOMAIN_OBJECTS.word import Word
from BUSINESS.SERVICES.APPLICATION_SERVICES.AI_AS.NLP_AS.NLP_AS_INTF.word_matcher_AS_intf import WordMatcherASIntf
from BUSINESS.SERVICES.APPLICATION_SERVICES.AI_AS.NLP_AS.NLP_AS_INTF.word_finder_AS_intf import WordFinderASIntf
from BUSINESS.SERVICES.APPLICATION_SERVICES.AI_AS.NLP_AS.NLP_AS_IMPL.word_finder_AS_impl import WordFinderASImpl
from BUSINESS.SERVICES.APPLICATION_SERVICES.AI_AS.NLP_AS.NLP_AS_INTF.word_corrector_AS_intf import WordCorrectorASIntf
from BUSINESS.SERVICES.APPLICATION_SERVICES.AI_AS.NLP_AS.NLP_AS_IMPL.word_corrector_AS_impl import WordCorrectorASImpl
from BUSINESS.CONSTRAINTS.CONVERTER.CONVERTER_INTF.text_normalizer_intf import TextNormalizerIntf
from BUSINESS.CONSTRAINTS.CONVERTER.CONVERTER_IMPL.text_normalizer_impl import TextNormalizerImpl


class WordMatcherASImpl(WordMatcherASIntf):

    def set_word_finder_as(self, word_finder_as: WordFinderASIntf):
        """

        :param word_finder_as: The Word Finder AS to be used by this current Word Matcher AS
        :return: None
        """
        self.word_finder_as = word_finder_as

    def get_word_finder_as(self) -> WordFinderASIntf:
        """
        
        :return: The Word Finder AS used by this current Word Matcher AS
        """
        return self.word_finder_as

    def set_word_corrector_as(self, word_corrector_as: WordCorrectorASIntf):
        """

        :param word_corrector_as: The Word Corrector AS to be used by this current Word Matcher AS
        :return: None
        """
        self.word_corrector_as = word_corrector_as

    def get_word_corrector_as(self) -> WordCorrectorASIntf:
        """

        :return: The Word Corrector AS used by this current Word Matcher AS
        """
        return self.word_corrector_as

    def set_text_normalizer(self, text_normalizer: TextNormalizerIntf):
        """

        :param text_normalizer: The Text Normalizer to be used by this Current Word Matcher AS
        :return: None
        """
        self.text_normalizer = text_normalizer

    def get_text_normalizer(self) -> TextNormalizerIntf:
        """

        :return: The Text Normalizer used by this Current Word Matcher AS
        """
        return self.text_normalizer

    def are_two_words_related(self, word_1: str, word_2: str):
        """

        :param word_1: The first "correct" Word for the Matching process
        :param word_2: The second "correct" Word for the Matching process
        :return: TRUE if the two words are related w.r.t their meanings, FALSE otherwise.
        """
        if word_1 and word_2:
            # We have non-blank words
            try:
                # First, let's normalize and then correct the two words,
                # and correct again but this time for the NLP's needs
                word_1_correct = self.get_word_corrector_as().correct(
                    self.get_text_normalizer().normalize(word_1)
                )
                word_2_correct = self.get_word_corrector_as().correct(
                    self.get_text_normalizer().normalize(word_2)
                )
                word_1_correct_for_nlp = self.get_text_normalizer().normalize_for_nlp(word_1_correct)
                word_2_correct_for_nlp = self.get_text_normalizer().normalize_for_nlp(word_2_correct)

                """
                Actual matching process part
                """
                if word_1_correct_for_nlp == word_2_correct_for_nlp:
                    # In the case where the two words provided are the same, they're consequently related
                    return True
                else:
                    # The two words aren't the same

                    # Generating the respective set of words neighbors of each word
                    words_1_neighbors = self.get_word_finder_as().find_word_close_neighbors(word_1_correct_for_nlp)\
                        .union(self.get_word_finder_as().find_word_likely_neighbors(word_1_correct_for_nlp))
                    words_2_neighbors = self.get_word_finder_as().find_word_close_neighbors(word_2_correct_for_nlp)\
                        .union(self.get_word_finder_as().find_word_likely_neighbors(word_2_correct_for_nlp))

                    # Now, let's combine word and its neighbors within a unique Word Object
                    word_object_1 = Word(word_1_correct_for_nlp)
                    word_object_1.set_associated_words(words_1_neighbors)
                    word_object_2 = Word(word_2_correct_for_nlp)
                    word_object_2.set_associated_words(words_2_neighbors)

                    """
                    Actual matching process part, in the case where the two words provided aren't the same
                    """
                    # The two words are related if they have at least one associated word in common,
                    # but if it isn't the case, they're therefore not related
                    matching_status = len(
                        word_object_1.get_associated_words().intersection(word_object_2.get_associated_words())
                    ) > 0
                    LOGGER.info(
                        "Matching status of the words : \"" + word_1 + "\" and \"" + word_2
                        + "\" : " + str(matching_status)
                    )
                    return matching_status
            except Exception as exception:
                # At least one error has occurred, therefore, stop the matching process
                LOGGER.error(
                    exception.__class__.__name__ + ": " + str(exception)
                    + ". Impossible matching process of the words : \"" + word_1 + "\" and \"" + word_2 + "\""
                )
                raise
        else:
            # At least one of the two words is blank or None
            LOGGER.info("At least one of the two words provided for the matching process is Blank or None")
            return None

    def __init__(self):
        # Initializing all the Application Services (ASs) & Text Normalizer to be used
        self.set_word_finder_as(WordFinderASImpl())
        self.set_word_corrector_as(WordCorrectorASImpl())
        self.set_text_normalizer(TextNormalizerImpl())
