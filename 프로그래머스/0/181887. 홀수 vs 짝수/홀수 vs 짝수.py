def solution(num_list):
    result_0 = 0
    result_1 = 0
    for i,num in enumerate(num_list):
        if i%2==0:
            result_0 += num
        else:
            result_1 += num
    return max(result_0, result_1)