def solution(num_list):
    odd_sum = ""
    even_sum = "" # 문자열
    
    for i in range(len(num_list)):
        if num_list[i]%2==1:
            odd_sum += str(num_list[i])
        else:
            even_sum += str(num_list[i])
    
    return int(odd_sum) + int(even_sum)