def solution(numbers, n):
    result = 0
    for num in numbers:
        result += num        # 하나 더하고
        if result > n:       # 합이 n보다 커지면
            return result    # 그 순간의 합을 반환
