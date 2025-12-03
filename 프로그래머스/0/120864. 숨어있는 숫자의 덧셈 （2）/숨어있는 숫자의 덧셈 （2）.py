import re

def solution(my_string):
    # 정규표현식 '[0-9]+' => "숫자가 1개 이상 연속된 것"을 찾으라
    numbers = re.findall(r'[0-9]+', my_string)
    
    # 찾은 문자열 숫자들을 정수(int)로 바꿔서 모두 더함
    return sum(map(int, numbers))