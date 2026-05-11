import unittest
import os
import csv
from lab7level2variant3 import calculate_max_cars


class TestFlowerFlow(unittest.TestCase):
    def setUp(self):
        self.test_filename = "temp_roads.csv"

    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def create_csv(self, farms, shops, roads):
        with open(self.test_filename, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(farms)
            writer.writerow(shops)
            for road in roads:
                writer.writerow(road)

    def test_simple_delivery(self):
        """Checking one direct path"""
        self.create_csv(["F1"], ["S1"], [["F1", "S1", "10"]])
        self.assertEqual(calculate_max_cars(self.test_filename), 10)

    def test_bottleneck(self):
        """Checking bandwidth limitation (bottleneck)"""
        self.create_csv(
            ["F1", "F2"], 
            ["S1"], 
            [
                ["F1", "X1", "10"],
                ["F2", "X1", "10"],
                ["X1", "S1", "5"]
            ]
        )
        self.assertEqual(calculate_max_cars(self.test_filename), 5)

    def test_multiple_paths(self):
        """Checking the flow distribution on different roads"""
        self.create_csv(
            ["F1"], 
            ["S1"], 
            [
                ["F1", "A", "5"],
                ["F1", "B", "7"],
                ["A", "S1", "5"],
                ["B", "S1", "7"]
            ]
        )
        self.assertEqual(calculate_max_cars(self.test_filename), 12)

    def test_no_connection(self):
        """Checking for the case where the path does not exist"""
        self.create_csv(["F1"], ["S1"], [["F1", "X1", "10"], ["X2", "S1", "10"]])
        self.assertEqual(calculate_max_cars(self.test_filename), 0)


if __name__ == "__main__":
    unittest.main()
