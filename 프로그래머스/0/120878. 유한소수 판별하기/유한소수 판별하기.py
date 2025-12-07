import math

def solution(a, b):
    # 1. 기약분수 만들기 - 최대공약수로 나누기
    gcd = math.gcd(a, b)
    b //= gcd # 분모 최대공약수로 나누기
    
    # 2. 분모에서 2제거
    while b % 2 ==0:
        b //=2 # 몫 구하기: //
        
    # 3. 분모에서 5제거
    while b % 5 ==0:
        b //=5
    
    # 4. 나머지가 1이면 유한소수
    if b ==1:
        return 1
    else:
        return 2
    
    
    answer = 0
    return answer