def solution(my_string):
    answer = 0
    for my in my_string:
        if my in "123456789":
            answer += int(my)
    return answer