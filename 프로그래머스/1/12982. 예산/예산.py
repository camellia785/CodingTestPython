def solution(d, budget):
    d = sorted(d)
    sum_d = 0
    count = 0
    
    for i in range(len(d)):
        sum_d += d[i]
        if sum_d <= int(budget):
            count += 1
            
    return count