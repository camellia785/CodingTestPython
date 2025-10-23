def solution(num_list):
    e_list =[]
    o_list =[]
    for n in num_list:
        if n % 2 ==0:
            e_list.append(n)
        else:
            o_list.append(n)
    return[len(e_list), len(o_list)]