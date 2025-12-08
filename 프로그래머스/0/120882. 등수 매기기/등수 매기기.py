def solution(score):
    #1. 평균저장리스트 avg
    avg = [(s[0] + s[1])/2 for s in score]
        
    #2. 평균점수를 내림차순(큰->작은)으로 정렬한 리스트
    sorted_avg = sorted(avg, reverse=True)
    result = []
    
    #3. 각 학생 등수 반환
    for a in avg:
        # 리스트 index()는 첫번째 등장 위치를 반환
        # 공동 등수 처리가 자동으로 됨
        
        rank = sorted_avg.index(a) +1
        result.append(rank)
        
    return result