def solution(array):
    counting = [0]*(max(array)+1) # 1. 갯수셀 빈칸 counting 만들기
    
    for a in array:
        counting[a] +=1
        
    max_count = max(counting) # 2. 최댓값 정의
        
    if counting.count(max_count) >1: #3. 갯수세기
        return -1
    else:
        return counting.index(max_count) #4. 인덱스값리턴