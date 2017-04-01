from unittest import TestCase
from square_of_numbers import squareOfNumbers

class TestSquareOfNumbers(TestCase):
    def test_squareOfNumbers(self):
        result = squareOfNumbers(8)
        self.assertEqual(result[1], 1)
        self.assertEqual(result[2], 4)
        self.assertEqual(result[3], 9)
        self.assertEqual(result[4], 16)
        self.assertEqual(result[5], 25)
        self.assertEqual(result[6], 36)
        self.assertEqual(result[7], 49)
        self.assertEqual(result[8], 64)
