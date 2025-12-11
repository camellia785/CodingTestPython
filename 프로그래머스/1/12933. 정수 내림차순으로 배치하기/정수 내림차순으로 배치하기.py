def solution(n):
    new = list(str(n))
    answer_list = sorted(new, reverse=True)
    return int("".join(answer_list))