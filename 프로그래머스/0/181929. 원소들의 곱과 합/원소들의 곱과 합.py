def solution(num_list):
    n = len(num_list)
    result = 1
    sum = 0
    
    for i in range(n):
        result *= num_list[i]
        sum += num_list[i]
        
    if result < sum**2:
        return 1
    else:
        return 0