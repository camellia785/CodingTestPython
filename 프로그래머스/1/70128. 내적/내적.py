def solution(a, b):
    mylist =[]
    for i in range(len(a)):
        mylist.append(a[i]*b[i])
        
    return sum(mylist)