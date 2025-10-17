def solution(picture, k):
    result=[]
    for p in picture:
        # 한줄 확대
        new_line = ''.join( [point*k for point in p] )
        
        # 세로 확대
        for _ in range(k):
            result.append(new_line)
        
    return result