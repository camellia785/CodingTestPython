def solution(array, n):
    count = 0
    for a in array:
        if a == n:
            count +=1
    return count