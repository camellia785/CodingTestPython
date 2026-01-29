def solution(s):
    result = []
    last_index = {} #딕셔너리 (2차원 넣을생각하기)
    
    for i, char in enumerate(s): # enumerate로 인덱스, 문자 한번에 가져오기
        if char in last_index:
            result.append(i - last_index[char])
        else:
            result.append(-1)
        # 갱신    
        last_index[char] = i
        
    return result
        
        