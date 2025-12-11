def solution(x):
    result = 0

    for s in str(x):
        result += int(s)
    
    if x % result == 0:
        answer = True
    else:
        answer = False
        
    return answer