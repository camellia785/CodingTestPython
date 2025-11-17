def solution(array):
    result = 0
    for a in array:
        result += str(a).count('7')
    return result