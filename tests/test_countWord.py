from unittest import TestCase
from count_word import countWord


class TestCountWord(TestCase):
    def test_countWord(self):
        result = countWord('../files/testfile.txt', 'dummy')
        self.assertEqual(2, result)

        result1 = countWord('../files/testfile.txt', 'Lorem')
        self.assertEqual(2, result1)