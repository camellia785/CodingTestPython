def solution(n):
    sqrt_n = n**(1/2)
    if sqrt_n % 1 == 0:
        return 1
    return 2