def solution(my_string):
    answer = ''
    for my in my_string:
        if my == my.upper():
            answer += my.lower()
        else:
            answer += my.upper()
    return answer