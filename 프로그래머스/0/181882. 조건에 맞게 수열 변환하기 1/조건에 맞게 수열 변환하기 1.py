def solution(arr):
    new_arr = []
    for num in arr:
        if (num >= 50) and (num%2==0):
            new_arr.append(num/2) 
        elif (num < 50 ) and (num%2==1):
            new_arr.append(num*2)
        else:
            new_arr.append(num)
    return new_arr