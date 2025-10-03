def solution(myString, pat):
    newString = ""
    answer = 0  
    for ch in myString:
        if ch=="A":
            newString+= "B"
        else:
            newString+= "A"
    
    if pat in newString:
        answer = 1
    return answer