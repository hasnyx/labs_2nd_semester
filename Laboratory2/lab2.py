def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def is_feasible(stalls, cows_count, min_dist):
    count = 1
    last_pos = stalls[0]
    
    for i in range(1, len(stalls)):
        if stalls[i] - last_pos >= min_dist:
            count += 1
            last_pos = stalls[i]
            if count >= cows_count:
                return True
    return False

def get_max_min_distance(n, c, free_sections):
    if c > n or n == 0:
        return 0
    
    stalls = merge_sort(free_sections)
    
    low = 1
    high = stalls[-1] - stalls[0]
    result = 0
    
    while low <= high:
        mid = (low + high) // 2
        
        if is_feasible(stalls, c, mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1
            
    return result