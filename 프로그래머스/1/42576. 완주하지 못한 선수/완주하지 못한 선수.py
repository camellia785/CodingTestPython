from collections import Counter

def solution(participant, completion):
    p_count = Counter(participant) # Counter는 타입의 이름을 말하는 것
    c_count = Counter(completion)  # {키:밸류, 키:밸류} 로 저장되는 dict 형태
    answer = p_count - c_count
    
    print(answer.keys()) # dict_keys(['vinko'])
    print(list(answer.keys())) # ['vinko']
    
    # 딕셔너리에서 키 값만 모은 뭉치 -> 리스트 강제변환 -> 첫값
    return list(answer.keys())[0]