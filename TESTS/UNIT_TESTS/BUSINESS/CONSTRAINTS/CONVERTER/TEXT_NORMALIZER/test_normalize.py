# -*- coding: utf-8 -*-

"""
test_normalize.py: The python file dedicated to Unit Testing of the 
"BUSINESS.CONSTRAINTS.CONVERTER.CONVERTER_IMPL.text_normalizer_impl.TextNormalizerImpl.normalize()" function
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

import unittest


from BUSINESS.CONSTRAINTS.CONVERTER.CONVERTER_IMPL.text_normalizer_impl import TextNormalizerImpl


class TestNormalize(unittest.TestCase):

    def test_normalize(self):
        """
        GIVEN a raw and not yet normalized text provided as an input,
        WHEN the normalize() method of the TextNormalizerImpl is called, with the previous text as its parameter,
        THEN a correct "Normalized" version of this must be returned
        """
        text_normalizer_test = TextNormalizerImpl()

        """
        Testing "normalize()"
        """
        # Integrity
        assert text_normalizer_test.normalize(None) is None
        assert text_normalizer_test.normalize("a") == "a"
        # All characters must be in the Lower Case
        assert text_normalizer_test.normalize("AaaAa") == "aaaaa"
        # No punctuations
        assert text_normalizer_test.normalize(".") == ""
        assert text_normalizer_test.normalize("a.a") == "aa"
        # No numbers
        assert text_normalizer_test.normalize("a1a2") == "aa"
        # Correct use of white space characters
        assert text_normalizer_test.normalize("    a1    a2 ") == "a a"
        # Simulating Real Time uses
        text_real_time_use_simulation_1 = "    a1?a2:, ;  ??"
        assert text_normalizer_test.normalize(text_real_time_use_simulation_1) == "aa"
        text_real_time_use_simulation_2 = [
            # Raw Text
            "Python 3.0, released in 2008, was a major revision of the language that is "
            "not completely backward compatible and much Python 2 code does not run "
            "unmodified on Python 3. With Python 2’s end-of-life, only Python 3.6.x[30] "
            "and later are supported, with older versions still supporting e.g. Windows "
            "7 (and old installers not restricted to 64-bit Windows)."
            # Expected "Normalized" text
            , "python released in was a major revision of the language that is not "
              "completely backward compatible "
              "and much python code does not run unmodified on python with python s "
              "endoflife only python x and "
              "later are supported with older versions still supporting eg windows "
              "and old installers not restricted "
              "to bit windows"
        ]
        assert text_normalizer_test.normalize(text_real_time_use_simulation_2[0]) == text_real_time_use_simulation_2[1]
