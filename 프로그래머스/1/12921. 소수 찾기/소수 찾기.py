def solution(n):
    answer = 0
    
    # 소수찾기
    for i in range(2, n+1):
        is_prime = True # 소수라고 가정
        
        # 2부터 제곱근까지 확인
        for j in range(2, int(i**(0.5))+1 ):
            if i % j == 0:
                is_prime = False # 약수 하나라도 나오면
                break
        if is_prime:
            answer += 1
    
    return answer