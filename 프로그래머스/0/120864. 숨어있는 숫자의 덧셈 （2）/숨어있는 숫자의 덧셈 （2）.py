def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    
    # 숫자와 공백만 남게됨 -> 공백 기준으로 s를 잘라서 int씌우고 다 더하기
    return sum(int(i) for i in s.split())
