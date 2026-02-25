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