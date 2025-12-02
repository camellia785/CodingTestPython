def solution(dots):
    xs = [x for x,y in dots] # x값만 뽑아서 리스트로
    ys = [y for x,y in dots] # y값만 뽑아서 리스트로
    
    return (max(xs) - min(xs))* (max(ys)- min(ys))