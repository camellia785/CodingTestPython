def solution(arr, k):
    if k % 2==1:
        arr = [a*k for a in arr]
    else:
        arr = [a+k for a in arr]
    return arr