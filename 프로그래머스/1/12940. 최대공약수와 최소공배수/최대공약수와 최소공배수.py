import math

# 최소공배수 직접 구현
def lcm(a, b):
    return a * b // math.gcd(a, b)

def solution(n, m):
    return [math.gcd(n, m), lcm(n, m)]
