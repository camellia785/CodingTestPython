def solution(strArr):
    newArr =[]
    for i, st in enumerate(strArr):
        newArr.append(st.upper()) if i%2==1 else newArr.append(st.lower())
    return newArr