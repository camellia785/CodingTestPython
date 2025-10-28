def solution(n):
    answer = 1
    i = 1
    while answer <= (n/i):
        answer *= i
        i += 1
    return i-1