from unittest import TestCase
from errors import no_function_found, incorrect_output, succeed

class TestLetterAndDigit(TestCase):
    def test_letterAndDigit(self):
        try:
            from letter_digit import letterAndDigit
            result = letterAndDigit('hello world! 123')
            self.assertEqual(3, result['DIGITS'])
            self.assertEqual(10, result['LETTERS'])
            self.assertTrue(succeed("letterAndDigit"))
        except ImportError:
            self.assertFalse(no_function_found("letterAndDigit"))
        except AssertionError:
            self.assertFalse(incorrect_output())

