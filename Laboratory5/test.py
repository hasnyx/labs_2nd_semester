import unittest
from lab5level3variant3 import count_islands

class TestIslandCounter(unittest.TestCase):

    def test_example_from_image(self):
        grid = [
            [1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
            [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
            [0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
            [1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 1, 1, 1]
        ]
        self.assertEqual(count_islands(grid), 5)

    def test_no_islands(self):
        grid = [[0, 0], [0, 0]]
        self.assertEqual(count_islands(grid), 0)

    def test_diagonal_islands_as_one(self):
        grid = [
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]
        ]
        self.assertEqual(count_islands(grid), 1)

if __name__ == '__main__':
    unittest.main()