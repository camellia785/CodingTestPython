def solution(arr):
    new = []
    if len(arr) != 1:
        min_value = min(arr)
        for a in arr:
            if a != min_value:
                new.append(a)
        return new
        
    else:
        return [-1]
        