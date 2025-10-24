def solution(emergency):
    answer = []
    v_list = sorted(emergency, reverse=True)
    
    for e in emergency:
        answer.append(v_list.index(e) + 1)
    
    return answer