def solution(n):
    num_list = []
    for num in str(n):
        num_list.append(int(num))
    num_list.reverse()
    return num_list