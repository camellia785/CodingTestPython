def solution(emergency):
    v_list = sorted(emergency, reverse=True)
    return [v_list.index(e) + 1 for e in emergency]