def solution(array, n):
    array.sort()
    closest = array[0]
    
    min_diff = abs(array[0] - n)
    
    for num in array:
        diff = abs(num - n)
        if diff < min_diff:
            min_diff = diff
            closest = num
    return closest