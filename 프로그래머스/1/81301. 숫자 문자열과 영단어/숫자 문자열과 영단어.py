def solution(s):
    dic_num = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
    
    for i in range(0,10):
        if dic_num[i] in s: #영어로 적힌경우
            s = s.replace(dic_num[i], str(i))
    
    return int(s)