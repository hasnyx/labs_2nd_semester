import unittest
from lab1 import longest_peak

class TestLongestPeak(unittest.TestCase):
    
    def test_example_case(self):
        self.assertEqual(longest_peak([1, 3, 5, 4, 2, 8, 3, 7]), 5)

    def test_sorted_ascending(self):
        self.assertEqual(longest_peak([1, 2, 3, 4, 5]), 0)

    def test_sorted_descending(self):
        self.assertEqual(longest_peak([5, 4, 3, 2, 1]), 0)

    def test_two_elements(self):
        self.assertEqual(longest_peak([1, 2]), 0)

    def test_no_peaks(self):
        self.assertEqual(longest_peak([1, 2, 2, 2, 1]), 0)
        self.assertEqual(longest_peak([5, 2, 5]), 0) 
        self.assertEqual(longest_peak([1, 1, 1]), 0)

    def test_three_peaks(self):
        self.assertEqual(longest_peak([1, 7, 2, 10, 9, 8, 7, 12, 5]), 5)

if __name__ == "__main__":
    unittest.main()