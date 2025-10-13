def solution(arr):
    n = len(arr) # 6
    power = 1
    
    while power < n:
        power *= 2
        
    return arr + [0]* (power - n)