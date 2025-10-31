def solution(order):
    result = 0
    for o in str(order):
        if o in "369" :
            result +=1
    return result