def solution(n):
    sum = 0
    result=0
    
    if n%2!=0:
        for i in range(n+1):
            if i%2 !=0:
                sum += i
        return sum
    else:
        for i in range(n+1):
            if i%2 ==0:
                result += i**2
        return result
    