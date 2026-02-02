def solution(n, arr1, arr2):
    answer = []
    for a,b in zip(arr1, arr2): #1. arr 2개 zip으로 묶기
        merged = a | b #2. OR연산으로 묶기
        result = format(merged,f'0{n}b') #3. 0이용해서 n자리로 맞춰라
        line = result.replace("0"," ").replace("1", "#") #4. replace하기
        answer.append(line) #5. answer에 추가하기
    return answer