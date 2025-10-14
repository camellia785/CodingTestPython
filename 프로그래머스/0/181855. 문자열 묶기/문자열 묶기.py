def solution(strArr):
    newArr=[] #길이를 담은 리스트
    numArr=[] #유니크 값의 개수를 담은 리스트
    
    for s in strArr:
        newArr.append(len(s))
    
    # 중복제거 set(), 개수세기 count()
    for num in set(newArr):
        numArr.append(newArr.count(num))

    return max(numArr)