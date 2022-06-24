# -*- coding: utf-8 -*-

"""
word_corrector_AS_impl.py: The python file dedicated to the Implementation Class of NLP Application Service
for the spellings correction of word
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

import re

# For the entire set of implementations, the TextBlob Library is the chosen NLP tool here
from textblob import Word

from CONFIGURATIONS.logger import LOGGER
from BUSINESS.SERVICES.APPLICATION_SERVICES.AI_AS.NLP_AS.NLP_AS_INTF.word_corrector_AS_intf import WordCorrectorASIntf


def reduce_lengthening(word: str) -> str:
    """
    English words have a maximum of two (02) repeated characters, therefore, this function rip offs
    repeated characters more than 2.

    :param word: The word concerned by the reduction of lengthening
    :return: The version of the word with the lengthening reduced
    """
    if word is not None and len(word) > 0:
        # A non-empty word was provided
        try:
            regex_pattern_for_the_reduction = re.compile(r"(.)\1{2,}")
            word_treated = regex_pattern_for_the_reduction.sub(r"\1\1", word)
            LOGGER.info(
                "Lengthening of the word : "
                + "\"" + word + "\""
                + " successfully reduced, the new version of the word is : "
                + word_treated
            )
            return word_treated
        except Exception as ex:
            # At least one error has occurred, therefore the reduction process couldn't happen
            LOGGER.error(
                ex.__class__.__name__ + ": " + str(ex)
                + ". Impossible reduction of the lengthening of the word : \""
                + word + "\"."
            )
            raise
    else:
        # An empty word was provided, therefore, we return a blank string
        LOGGER.info("No word was provided for the lengthening reduction process")
        return ""


def correcting_spellings(word: str) -> str:
    """
    The actual function responsible for the actual part dedicated to the spellings correction of a given word.

    :param word: The word to be corrected w.r.t its spellings
    :return: The corrected version, w.r.t its spellings, of the word given in parameter
    """
    if word is not None and len(word) > 0:
        # The word provided wasn't empty

        # first, let's verify and manage if some abnormalities are found regarding the lengthening of the given word
        word_to_correct = Word(reduce_lengthening(word))
        # returning the "correct" word having the highest mark of correspondence with the given word
        word_corrected = word_to_correct.correct()
        LOGGER.info(
            "Word : "
            + "\"" + word + "\""
            + " corrected to : "
            + "\"" + word_corrected + "\""
        )
        return word_to_correct.correct()
    else:
        # An empty word was provided, so, just return a blank String
        LOGGER.info("No word was provided for the lengthening correction process")
        return ""


class WordCorrectorASImpl(WordCorrectorASIntf):
    def correct(self, word: str) -> str:
        """
        Correcting the Spelling of a word inserted within the parameter.

        :param word: The word to be corrected (w.r.t its Spelling)
        :return: The corrected version (w.r.t its Spelling) of the word inserted within the parameter
        """
        if (word is not None) and (len(word) > 0):
            # a non-empty word was provided
            word_corrected = correcting_spellings(word)
            LOGGER.info(
                "Word : "
                + "\"" + word + "\""
                + " successfully corrected to : "
                "\"" + word_corrected + "\""
            )
            return word_corrected
        # no word was provided, so let's return a blank string
        LOGGER.info("No word was provided for the correction")
        return ""
