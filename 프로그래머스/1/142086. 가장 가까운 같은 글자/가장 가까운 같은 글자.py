def solution(s):
    answer = []
    last_index = {} # 문자별 마지막 등장위치(숫자)
    
    for i in range(len(s)):
        char = s[i]
        
        if char not in last_index:
            answer.append(-1)
        else:
            answer.append(i - last_index[char])
            
        # 현재위치로 last_index 갱신
        last_index[char] = i
        
    return answer