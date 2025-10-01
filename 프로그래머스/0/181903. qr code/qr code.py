def solution(q, r, code):
    answer = ''
    for i in range(0, (len(code) // q) + 1):       
        if q*i + r < len(code):           
            answer += code[q*i + r]
    return answer