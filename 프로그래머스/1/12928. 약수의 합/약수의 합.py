def solution(n):
    an_list = []
    for i in range(1,n+1):
        if n % i ==0:
            an_list.append(i)
    return sum(an_list)