def solution(polynomial):
    # 1. 변수 세팅, +로 쪼개기
    terms = polynomial.split(" + ")
    x_sum = 0
    num_sum = 0
    
    # 2. 동류항끼리 계산
    for term in terms:
        if 'x' in term:
            # 계수가 없는경우 +1하기
            if term == 'x':
                x_sum += 1
            else:
                x_sum += int(term[:-1]) #숫자만 꺼내서 더하기
        
        else: # 상수항
            num_sum += int(term)
    
    # 3. 결과 조립
    result = []
    if x_sum:
        result.append("x" if x_sum == 1 else f"{x_sum}x")
    if num_sum:
        result.append(str(num_sum))
    
    return " + ".join(result)