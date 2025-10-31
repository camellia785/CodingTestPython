def solution(sides):
    temp = sides[:]
    temp.remove(min(sides))
    temp.remove(max(sides))
    
    mid = temp[0]
    return 1 if min(sides) + mid > max(sides) else 2