def solution(date1, date2):
    if date1[0] < date2[0]: 
        return 1
    
    elif date1[0] == date2[0]: #년도가 같다면
        if date1[1] < date2[1]:
            return 1
        
        elif date1[1] == date2[1]: #월이 같다면
            if date1[2] < date2[2]:
                return 1
    return 0

#간단풀이
#return int(date1 < date2)
