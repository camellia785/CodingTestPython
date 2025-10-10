def solution(arr, k):
    new = []
    for a in arr:
        if a not in new:
            new.append(a) 
        if len(new) == k:
            break
    while len(new) < k:
        new.append(-1)
    
    return new