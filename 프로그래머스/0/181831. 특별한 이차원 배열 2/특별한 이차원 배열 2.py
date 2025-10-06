def solution(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] != arr[j][i]: # 하나라도 다르면 비대칭
                return 0
    return 1 # 모두 통과하면 대칭