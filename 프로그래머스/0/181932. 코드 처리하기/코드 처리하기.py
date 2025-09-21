def solution(code):
    ret = []
    mode = 0
    
    # enumerate로 index, char 한번에 가져오기
    for idx, char in enumerate(code):
        if char =='1':
            mode = 1-mode
        else:
            if idx % 2 == mode:
                ret.append(char)
        
    result = "".join(ret)
    
    return result if result else "EMPTY"