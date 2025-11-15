def solution(array):
    answer = []
    M = max(array)
    answer.append(M)
    answer.append(array.index(M))
    return answer