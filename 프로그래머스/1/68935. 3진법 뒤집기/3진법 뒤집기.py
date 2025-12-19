def solution(n):
    ternary = ""
    
    while n > 0: #n보다 큰 동안
        ternary += str(n%3)
        n //= 3
        
    return int(ternary,3) # 3진법 tenary를 int씌워서 10진법으로 만들겠다

    