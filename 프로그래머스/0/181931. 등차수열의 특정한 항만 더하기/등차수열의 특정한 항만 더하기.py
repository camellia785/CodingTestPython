def solution(a, d, included):
    n = len(included)
    sum = 0
    for i in range(0,n):
        if included[i]:
            sum += a+i*d
    return sum