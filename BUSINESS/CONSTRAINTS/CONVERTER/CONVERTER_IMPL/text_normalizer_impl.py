# -*- coding: utf-8 -*-

"""
text_normalizer_impl.py: The python file dedicated to the Implementation Class for the text normalization process
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

import re

from CONFIGURATIONS.logger import LOGGER

from BUSINESS.CONSTRAINTS.CONVERTER.CONVERTER_INTF.text_normalizer_intf import TextNormalizerIntf


class TextNormalizerImpl(TextNormalizerIntf):

    def normalize(self, text_to_normalize: str) -> str:
        """
        Transforming a text into one canonical form, this latter chosen according to the specific need within the Dobryy Sokil Project.

        :param text_to_normalize: The text to normalize
        :return: The normalized version of the text put in parameter
        """
        if text_to_normalize is not None:  # Text made up of only one Blank Character considered as a valid one
            try:
                # STEP 1 : Converting all the letters to Lower Case
                text_normalized = text_to_normalize.lower()

                # STEP 2 : Assuming that they are not relevant enough for the understanding process of the text
                # to be normalized, let's remove all the Numbers
                text_normalized = re.sub(r'\d+', '', text_normalized)

                # STEP 3: Assuming that they are not relevant enough for the understanding process of the text
                # to be normalized, just like with the Numbers, let's remove all the Punctuations
                text_normalized = re.sub(r'[^\w\s]', '', text_normalized)

                # STEP 4: Regulating the use of white space within the text
                # Removing all white space characters on the both ends of the text
                text_normalized = text_normalized.strip()
                # Substituting all consecutive white space characters by only one
                text_normalized = re.sub('\s+', ' ', text_normalized)

                # The text was successfully normalized
                LOGGER.info(
                    "\"" + text_to_normalize + "\""
                    + " successfully normalized to : "
                    + "\"" + text_normalized + "\""
                )
                return text_normalized
            except Exception as exception:
                # At least one error has occurred, therefore, stop the normalization process
                LOGGER.error(
                    exception.__class__.__name__ + ": " + str(exception)
                    + ". Impossible normalization of the text : \""
                    + text_to_normalize + "\"."
                )
                raise
        else:
            # No input text was provided
            LOGGER.info("No text was provided.")
            return None

    def normalize_for_nlp(self, text_to_normalize: str) -> str:
        """
        Firstly, transforming a text into one canonical form, this latter chosen according to the specific needs
        within the Dobryy Sokil Project.
        Secondly, transforming the previous normalized text to another version according to the specific needs for
        NLP.

        :param text_to_normalize: The text to normalize
        :return: The NLP-normalized version of the text put in parameters
        """
        if text_to_normalize is not None:  # Text made up of only one Blank Character considered as a valid one
            try:
                # Normalizing according to the general canonical form
                text_normalized = self.normalize(text_to_normalize)

                """
                Normalizing according to the NLP needs
                """
                # "Space" characters are replaced by "_"
                text_nlp_normalized = text_normalized.replace(" ", "_")
                # The text was successfully normalized
                LOGGER.info(
                    "\"" + text_to_normalize + "\""
                    + " successfully normalized for NLP to : "
                    + "\"" + text_nlp_normalized + "\""
                )
                return text_nlp_normalized
            except Exception as exception:
                # At least one error has occurred, therefore, stop the normalization process
                LOGGER.error(
                    exception.__class__.__name__ + ": " + str(exception)
                    + ". Impossible NLP normalization of the text : \""
                    + text_to_normalize + "\"."
                )
                raise
        else:
            # No input text was provided
            LOGGER.info("No text was provided.")
            return None
