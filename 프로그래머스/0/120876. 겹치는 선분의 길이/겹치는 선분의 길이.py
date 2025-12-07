def solution(lines):
    counts = [0] * 201 # 음수는 배열안되니까 0~200으로 counts
    
    for start, end in lines:
        for x in range(start, end):
            counts[x+100] += 1
    
    answer = 0
    for c in counts:
        if c >= 2: # 두개이상이면 추가
            answer += 1
    
    return answer