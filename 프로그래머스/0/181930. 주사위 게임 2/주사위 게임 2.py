def solution(a, b, c):
    score = 0
    
    if (a != b) and (b != c) and (c != a):
        score = a+b+c 
    elif (a == b == c):
        score = (a+b+c)*(a**2 + b**2 + c**2)*(a**3+b**3+c**3)
    else:
        score = (a+b+c)*(a**2 + b**2 + c**2)
    
    return score