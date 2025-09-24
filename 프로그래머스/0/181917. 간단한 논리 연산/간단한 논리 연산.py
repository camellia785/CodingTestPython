def solution(x1, x2, x3, x4):
    if (x1 or x2) == True and (x3 or x4) == True:
        return True
    else:
        return False
    
# 간단한 논리연산 
# def solution(x1, x2, x3, x4):
#     return (x1 or x2) and (x3 or x4)