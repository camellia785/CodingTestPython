def solution(numbers):
    answer = []
    dupli = []
    
    # 두개 뽑고 더하고
    for i in numbers:
        for j in numbers:
            answer.append(i+j)
    
    # 자기 두번 더해서 나온거 제외하기 (단순차집합 하면 다 빠지니까 remove하기)
    for k in numbers:
        dupli.append(2*k)
    
    for x in dupli:
        if x in answer:
            answer.remove(x)
    
    # 마지막 중복제거
    answer = list(set(answer))

    return sorted(answer)