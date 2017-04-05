from unittest import TestCase
from errors import succeed, incorrect_output, no_function_found


class TestSquareOfNumbers(TestCase):
    def test_squareOfNumbers(self):
        try:
            from square_of_numbers import squareOfNumbers
            result = squareOfNumbers(8)
            if isinstance(result, dict):
                self.assertEqual(result[1], 1)
                self.assertEqual(result[2], 4)
                self.assertEqual(result[3], 9)
                self.assertEqual(result[4], 16)
                self.assertEqual(result[5], 25)
                self.assertEqual(result[6], 36)
                self.assertEqual(result[7], 49)
                self.assertEqual(result[8], 64)
                self.assertTrue(succeed("squareOfNumbers"))
            else:
                self.assertFalse(incorrect_output())
        except ImportError:
            self.assertFalse(no_function_found("squareOfNumbers"))
        except AssertionError:
            self.assertFalse(incorrect_output())