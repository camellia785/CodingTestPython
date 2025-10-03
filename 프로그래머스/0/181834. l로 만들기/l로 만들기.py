import string

def solution(myString):
    before_l = [ch for ch in string.ascii_lowercase if ch < "l"]
    
    result = ""
    for ch in myString:
        if ch in before_l:
            result += "l"
        else:
            result += ch
    
    return result