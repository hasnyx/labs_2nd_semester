import unittest
from lab2 import get_max_min_distance

class TestAggressiveCows(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(get_max_min_distance(5, 3, [1, 2, 8, 4, 9]), 3)

    def test_all_cows_same_dist(self):
        self.assertEqual(get_max_min_distance(3, 3, [0, 5, 10]), 5)

    def test_two_cows_extremes(self):
        self.assertEqual(get_max_min_distance(5, 2, [10, 2, 5, 1, 8]), 9)

if __name__ == '__main__':
    unittest.main()