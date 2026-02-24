import unittest

def longest_peak(array):
    longest_peak_length = 0
    i = 1
    
    while i < len(array) - 1:
        is_peak = array[i] > array[i - 1] and array[i] > array[i + 1]
        
        if not is_peak:
            i += 1
            continue
        
        left_idx = i - 2
        while left_idx >= 0 and array[left_idx] < array[left_idx + 1]:
            left_idx -= 1
            
        right_idx = i + 2
        while right_idx < len(array) and array[right_idx] < array[right_idx - 1]:
            right_idx += 1
            
        current_peak_length = right_idx - left_idx - 1
        longest_peak_length = max(longest_peak_length, current_peak_length)
        
        i = right_idx
        
    return longest_peak_length

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