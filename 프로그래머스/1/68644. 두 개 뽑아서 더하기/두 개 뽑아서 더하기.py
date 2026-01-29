def solution(numbers):
    answer = []
    
    #nC2 로 나오는애들 더하는거 구하는법
    for i in range(len(numbers)): # 0,1,2,3,4
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i]+numbers[j])

    return sorted(list(set(answer)))