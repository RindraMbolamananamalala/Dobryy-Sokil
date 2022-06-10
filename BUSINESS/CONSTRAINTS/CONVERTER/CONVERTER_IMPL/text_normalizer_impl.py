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

from BUSINESS.CONSTRAINTS.CONVERTER.CONVERTER_INTF.text_normalizer_intf import TextNormalizerIntf


class TextNormalizerImpl(TextNormalizerIntf):
    def normalize(self, text_to_normalize: str):
        """
        Transforming a text into one canonical form, this latter chosen according to the specific needs
        within the Dobryy Sokil Project.
        :param text_to_normalize: The text to normalize
        :return: the normalized version of the text put in parameter
        """

        # STEP 1 : Converting all the letters to Lower Case
        text_normalized = text_to_normalize.lower()

        # STEP 2 : Assuming that they are not sufficiently relevant to the understanding process of the text
        # to be normalized, let's remove all the Numbers
        text_normalized = re.sub(r'\d+', '', text_normalized)

        # STEP 3: Assuming that they are not sufficiently relevant to the understanding process of the text
        # to be normalized, just like with the Numbers, let's remove all the Punctuations
        text_normalized = re.sub(r'[^\w\s]', '', text_normalized)

        # STEP 4: Regulating the use of white space within the text
        text_normalized = text_normalized.strip()

        return text_normalized

