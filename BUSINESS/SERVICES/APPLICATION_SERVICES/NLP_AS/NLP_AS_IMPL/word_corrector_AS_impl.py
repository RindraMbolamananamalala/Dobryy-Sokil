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
from BUSINESS.SERVICES.APPLICATION_SERVICES.NLP_AS.NLP_AS_INTF.word_corrector_AS_intf import WordCorrectorASIntf


def reduce_lengthening(word: str) -> str:
    try:
        """
        English words have a maximum of two (02) repeated characters, therefore, this function rip offs
        repeated characters more than 2.
        :param word: The word concerned by the reduction of lengthening
        :return: The version of the word with the lengthening reduced
        """
        regex_pattern_for_the_reduction = re.compile(r"(.)\1{2,}")
        return regex_pattern_for_the_reduction.sub(r"\1\1", word)
    except Exception as ex:
        print(str(ex))
        return None


def correcting_spellings(word: str) -> str:
    """
    The actual function responsible for the actual part dedicated to the spellings correction of a given word.
    :param word: The word to be corrected w.r.t its spellings
    :return: The corrected version, w.r.t its spellings, of the word given in parameter
    """
    # first, let's verify and manage if some abnormalities are found regarding the lengthening of the given word
    word_to_correct = Word(reduce_lengthening(word))
    # returning the "correct" word having the highest mark of correspondence with the given word
    word_corrected = word_to_correct.correct()

    LOGGER.info("\"" + word + "\"" + " corrected to : " + "\"" + word_corrected + "\"")
    return word_to_correct.correct()


class WordCorrectorASImpl(WordCorrectorASIntf):
    def correct(self, word: str) -> str:
        """
        Correcting the Spelling of a word inserted within the parameter.
        :param word: The word to be corrected (w.r.t its Spelling)
        :return: The corrected version (w.r.t its Spelling) of the word inserted within the parameter
        """
        if (word is not None) and (len(word) > 0):
            return correcting_spellings(word)
        # no word was provided, so let's return a blank string
        LOGGER.info("No word was provided for the correction")
        return ""
