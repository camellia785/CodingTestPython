def solution(t, p):
    count = 0 
    
    for i in range(len(t)-len(p)+1):
        # 문자열 슬라이싱
        sub = int(t[i:i+len(p)])
        if sub <= int(p):
            count += 1
            
    return count