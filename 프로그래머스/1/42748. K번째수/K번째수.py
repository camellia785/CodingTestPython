def solution(array, commands):
    answer = []
    
    for i,j,k in commands:
        temp = sorted((array[i-1:j])) # sorted()가 반환값존재
        answer.append(temp[k-1]) # temp로 array 건들지 X
        
    return answer