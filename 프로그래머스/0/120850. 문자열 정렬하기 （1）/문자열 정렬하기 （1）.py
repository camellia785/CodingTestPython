def solution(my_string):
    answer = []
    for my in my_string:
        if my in "1234567890":
            answer.append(int(my))
        answer.sort()
    return answer