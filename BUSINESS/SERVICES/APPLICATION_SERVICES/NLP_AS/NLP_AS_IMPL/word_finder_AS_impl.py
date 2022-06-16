# -*- coding: utf-8 -*-

"""
word_finder_AS_impl.py: The python file dedicated to the Implementation Class of NLP Application Service
for any finding process related to words
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

# For the entire set of implementations, the TextBlob Library is the chosen NLP tool here
from textblob import Word

from BUSINESS.SERVICES.APPLICATION_SERVICES.NLP_AS.NLP_AS_INTF.word_finder_AS_intf import WordFinderASIntf


def find_word_synonyms(word: str) -> set():
    """
    :param word: The word whose synonyms are to be found
    :return: - The set of synonyms related to the word given in parameter
    - Directly a blank set if the given word is None or empty
    """
    synonyms = set()
    if word is not None and len(word) > 0:
        concerned_word = Word(word)
        for synonyms_set in concerned_word.synsets:
            for lemma in synonyms_set.lemmas():
                synonyms.add(lemma.name())
        # For sure, it is likely that the word itself has been considered as its own close neighbors
        # during the collect of all the Lemmas related to its synonyms, therefore, if it is the case,  we have to remove
        # it from the set of neighbors to return.
        synonyms.discard(word)
        return synonyms
    # The word is None or its length is inferior to 1
    return synonyms


def find_word_s_neighbors_synonyms(word: str) -> set():
    """
    :param word: The word whose synonyms of close neighbors are to be retrieved
    :return: The set of synonyms of the close neighbors related to the word given in parameter, OR Directly a blank set if the given word is None or empty
    """
    neighbors_synonyms = set()
    if word is not None and len(word) > 0:
        for related_word in find_word_synonyms(word):
            neighbors_synonyms = find_word_synonyms(related_word).union(neighbors_synonyms)
        # For sure, it is likely that the word given in parameter itself has been considered as a synonym
        # of one or more of the words retrieved as being its close neighbors, so, we have to remove it from
        # the set of results to be returned
        neighbors_synonyms.discard(word)
        return neighbors_synonyms
    # The word is None or its length is inferior to 1
    return neighbors_synonyms


class WordFinderASImpl(WordFinderASIntf):

    def find_word_close_neighbors(self, word: str) -> set():
        """
        Finding the set of words that can be considered, with "high" confidence, as neighbors of a given "correct" word.
        :param word: The word whose neighbors are to be found
        :return: The list of words that are the neighbors, with "high" confidence, of the word given within the parameter
        """
        # Any word that is a synonym and any word that is "directly" related to the concerned word is
        # "Highly" considered as its close neighbor
        word_synonyms = find_word_synonyms(word)
        return word_synonyms

    def find_word_likely_neighbors(self, word: str) -> set():
        """
        Finding the set of words that can be considered, with "relatively high" confidence, as neighbors of a given
        "correct" word.
        :param word: The word whose neighbors are to be found
        :return: The list of words that are the neighbors, with "relatively high" confidence, of the word given within
        the parameter
        """
        # Any word that is a synonym of a "close" neighbor of the word given in parameter is
        # "Relatively Highly" considered as the latter' s likely neighbor
        return find_word_s_neighbors_synonyms(word)

