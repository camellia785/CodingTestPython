import numpy as np

def solution(n):
    arr = np.zeros((n,n), dtype=int)
    for i in range(n):
        arr[i][i] = 1 # 대각선
    return arr.tolist() #tolist()를 통해, arr를 list 변환