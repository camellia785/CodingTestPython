def solution(a, b):
    if a > b:
        a, b = b, a #할당 연산자 =
    return sum(range(a, b+1))