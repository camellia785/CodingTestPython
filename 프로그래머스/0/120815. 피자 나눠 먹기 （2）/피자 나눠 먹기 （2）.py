def solution(n):
    for i in range(1, 101):
        if (n * i) % 6 == 0:
            return n * i / 6