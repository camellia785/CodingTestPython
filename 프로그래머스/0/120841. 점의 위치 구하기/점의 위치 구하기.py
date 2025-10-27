def solution(dot):
    x, y = dot[0], dot[1]
    if x > 0:
        return 1 if y >0 else 4
    elif x<0:
        return 2 if y >0 else 3