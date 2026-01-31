def solution(k, score):
    answer = []
    top_list = []
    
    for i, s in enumerate(score):
        top_list.append(s)
        top_list = sorted(top_list, reverse=True)[:k]
        answer.append(min(top_list))
    
    return answer