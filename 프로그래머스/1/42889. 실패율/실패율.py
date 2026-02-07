def solution(N, stages):
    result = {} #딕셔너리 형태로 정의
    people = len(stages) 
    
    # 1. 실패율 계산
    for stage in range(1, N+1):
        if people != 0:
            count = stages.count(stage)
            result[stage] = count / people
            people -= count
        else:
            result[stage] = 0
    
    # sort해서 반환
    return sorted(result, key=lambda x : result[x], reverse=True)