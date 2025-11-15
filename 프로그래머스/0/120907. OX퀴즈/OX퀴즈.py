def solution(quiz):
    result =[]
    
    for q in quiz:
        L, R = q.split("=")
        
        if eval(L) == int(R):
            result.append("O")
        else:
            result.append("X")
    
    return result