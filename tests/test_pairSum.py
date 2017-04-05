from unittest import TestCase
from errors import no_function_found, succeed

class TestPairSum(TestCase):
    def test_pairSum(self):
        try:
            from pair_sum import pairSum
            result = pairSum([2, 5, 4, 3, 8, 7, 6, 1, 10, -1], 9)
            for item in result:
                self.assertEqual(9, (item[0] + item[1]))
            self.assertTrue(succeed("pairSum"))
        except ImportError:
            self.assertFalse(no_function_found("pairSum"))