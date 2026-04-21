import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from lab6level3variant3 import find_unreachable_cities


class TestGasPipelines(unittest.TestCase):
    def setUp(self):
        """Initial data for testing using Ukrainian city names."""
        self.cities = ["Львів", "Стрий", "Долина"]
        self.storages = ["Сховище_1", "Сховище_2"]

    def test_all_cities_reachable(self):
        """Test Case 1: All cities are reachable from all storages."""
        pipelines = [
            ["Сховище_1", "Львів"],
            ["Львів", "Стрий"],
            ["Стрий", "Долина"],
            ["Сховище_2", "Долина"],
            ["Долина", "Львів"],
        ]
        result = find_unreachable_cities(self.cities, self.storages, pipelines)
        self.assertEqual(result, [])

    def test_some_cities_unreachable(self):
        """Test Case 2: Storage_1 cannot deliver gas to Dolyna."""
        pipelines = [
            ["Сховище_1", "Львів"],
            ["Львів", "Стрий"],
        ]
        result = find_unreachable_cities(self.cities, self.storages, pipelines)
        
        self.assertEqual(result[0][0], "Сховище_1")
        self.assertIn("Долина", result[0][1])

    def test_transit_delivery(self):
        """Test Case 3: Verify transit delivery (Storage_A -> Stryi -> Lviv)."""
        cities = ["Львів", "Стрий"]
        storages = ["Сховище_А"]
        pipelines = [["Сховище_А", "Стрий"], ["Стрий", "Львів"]]

        result = find_unreachable_cities(cities, storages, pipelines)
        self.assertEqual(result, [])

    def test_no_active_pipelines(self):
        """Test Case 4: Scenario where all pipelines are under repair."""
        pipelines = []
        result = find_unreachable_cities(self.cities, self.storages, pipelines)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0][0], "Сховище_1")
        self.assertEqual(set(result[0][1]), set(self.cities))


if __name__ == "__main__":
    unittest.main()