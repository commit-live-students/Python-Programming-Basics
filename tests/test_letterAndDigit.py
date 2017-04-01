from unittest import TestCase
from letter_digit import letterAndDigit

class TestLetterAndDigit(TestCase):
    def test_letterAndDigit(self):
        result = letterAndDigit('hello world! 123')
        self.assertEqual(3, result['DIGITS'])
        self.assertEqual(10, result['LETTERS'])
