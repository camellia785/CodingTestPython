def solution(n):
    count = 0 # 3x에서 허용되는 숫자 개수 세기
    num = 0 # 실제 숫자
    
    while count < n:
        num += 1
        
        if num%3== 0 or '3' in str(num):
            continue
        count += 1
        
    return num