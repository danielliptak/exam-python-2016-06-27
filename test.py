import unittest
from third import *

class TestExtend(unittest.TestCase):
    def test_result_is_number(self):
        self.assertIsInstance(count_letter_in_string('bableves', 'h'), int)
    def test_result_is_string(self):
        self.assertEqual(count_letter_in_string(7, 'h'), 0)
    def test_count_well(self):
        self.assertEqual(count_letter_in_string('elkelkaposztastalanithatatlansagaitokert', 'e'), 3)

if __name__ == '__main__':
    unittest.main()
