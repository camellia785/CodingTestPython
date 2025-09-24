def solution(a, b, c, d):
    dice = [a,b,c,d]
    s = set(dice) # 중복제거
    l = len(s)
    
    # case 1 한가지 값
    if l == 1:
        return 1111*a
    
    # case 2 두가지 값 ( 1+3, 2+2)
    elif l == 2:
        for x in s:
            if dice.count(x) ==3:
                p, q = x, (s-{x}).pop()
                return (10*p + q) **2
        p, q = list(s)
        return (p+q) * abs(p-q)
    
    # case 3 세가지 값 (1+1+2)
    elif l ==3:
        for x in s:
            if dice.count(x) ==2:
                others = list(s - {x})
                return others[0] *others[1]
    
    else:
        return min(dice)