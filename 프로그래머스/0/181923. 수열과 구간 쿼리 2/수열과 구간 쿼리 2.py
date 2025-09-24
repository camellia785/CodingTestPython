def solution(arr, queries):
    result = []
    
    for s, e, k in queries:  
        candidates = [arr[i] for i in range(s, e+1) if arr[i]>k]
        if candidates:
            result.append(min(candidates))
        else:
            result.append(-1)
    return result