def solution(n):
    result = []
    result.append(n)
    while n != 1:
        if n%2==0:
            n = n/2
            result.append(n)
        else:
            n = 3*n+1
            result.append(n)
                
    return result