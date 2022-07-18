# -*- coding: utf-8 -*-

"""
test_normalize_for_nlp.py: The python file dedicated to Unit Testing of the
"BUSINESS.CONSTRAINTS.CONVERTER.CONVERTER_IMPL.text_normalizer_impl.TextNormalizerImpl.normalize_for_nlp()" function
"""

__author__ = "Rindra Mbolamananamalala"
__version__ = "1.0.1"
__maintainer__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"
__status__ = "Prototype"

import unittest

from BUSINESS.CONSTRAINTS.CONVERTER.CONVERTER_IMPL.text_normalizer_impl import TextNormalizerImpl


class TestNormalizeForNLP(unittest.TestCase):

    def test_normalize_for_nlp(self):
        """
        GIVEN a raw and not yet NLP-normalized text provided as an input,
        WHEN the normalize_for_nlp() method of the TextNormalizerImpl is called, with the previous text as its parameter,
        THEN a correct "NLP-Normalized" version of this must be returned
        """

        # Preparing the Text Normalizer for the test
        text_normalizer_test = TextNormalizerImpl()

        # Integrity
        assert text_normalizer_test.normalize_for_nlp(None) is None
        assert text_normalizer_test.normalize_for_nlp("a") == "a"
        # All characters must be in the Lower Case
        assert text_normalizer_test.normalize_for_nlp("AaaAa") == "aaaaa"
        # No punctuations
        assert text_normalizer_test.normalize_for_nlp(".") == ""
        assert text_normalizer_test.normalize_for_nlp("a.a") == "aa"
        # No numbers
        assert text_normalizer_test.normalize_for_nlp("a1a2") == "aa"
        # Correct use of white space characters
        assert text_normalizer_test.normalize_for_nlp("    a1    a2 ") == "a_a"
        assert text_normalizer_test.normalize_for_nlp("aaaa   a            ab      cc") == "aaaa_a_ab_cc"
        assert text_normalizer_test.normalize_for_nlp("a_a_a") == "a_a_a"
        assert text_normalizer_test.normalize_for_nlp("a_a_ _a") == "a_a___a"

        # Simulating Real Time uses
        text_real_time_use_simulation_1 = "    a1?a2:, _;    _??"
        assert text_normalizer_test.normalize_for_nlp(text_real_time_use_simulation_1) == "aa____"
        text_real_time_use_simulation_2 = [
            # Raw Text
            "Python 3.0, released in 2008, was a major revision of the language that is "
            "not completely backward compatible and much Python 2 code does not run "
            "unmodified on Python 3. With Python 2’s end-of-life, only Python 3.6.x[30] "
            "and later are supported, with older versions still supporting e.g. Windows "
            "7 (and old installers not restricted to 64-bit Windows)."
            # Expected "Normalized" text
            , "python_released_in_was_a_major_revision_of_the_language_that_is_not_"
              "completely_backward_compatible_"
              "and_much_python_code_does_not_run_unmodified_on_python_with_python_s_"
              "endoflife_only_python_x_and_"
              "later_are_supported_with_older_versions_still_supporting_eg_windows_"
              "and_old_installers_not_restricted_"
              "to_bit_windows"
        ]
        assert text_normalizer_test.normalize_for_nlp(text_real_time_use_simulation_2[0]) == \
               text_real_time_use_simulation_2[1]
