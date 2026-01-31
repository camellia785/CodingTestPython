from collections import Counter

def solution(participant, completion):
    # {키:밸류, 키:밸류} 로 저장되는 dict 형태
    p_count = Counter(participant)
    c_count = Counter(completion)
    
    answer = p_count - c_count
    
    # 딕셔너리에서 키 값만 모은 뭉치 -> 리스트 강제변환 -> 첫값
    return list(answer.keys())[0]
    
    