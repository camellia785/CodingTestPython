def solution(balls, share):
    son = 1
    mom1 = 1
    mom2 = 1
    
    for i in range(1, balls+1):
        son *= i
    for j in range(1, balls-share+1):
        mom1 *= j
    for k in range(1, share+1):
        mom2 *= k
    
    
    return son/(mom1*mom2)