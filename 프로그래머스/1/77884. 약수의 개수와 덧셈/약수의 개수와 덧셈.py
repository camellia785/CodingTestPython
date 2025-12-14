def solution(left, right):
    sum_list = []
    for num in range(left, right+1):
        i_list = []
        for i in range(1, num+1):
            if num % i == 0:
                i_list.append(i)
        if len(i_list) % 2 ==0:
            sum_list.append(num)
        else:
            sum_list.append(-num)

    return sum(sum_list)