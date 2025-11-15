def solution(num, k):
    str_num = str(num)
    str_k = str(k)
    
    for i in range(0,len(str_num)):
        if str_num[i] == str_k:
            return int(i)+1
        
    return -1