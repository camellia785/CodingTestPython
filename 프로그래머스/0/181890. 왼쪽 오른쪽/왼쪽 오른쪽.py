def solution(str_list):
    answer = []
    
    if "l" in str_list and "r" in str_list:
        if str_list.index("l") < str_list.index("r"):
            answer = str_list[:str_list.index("l")]
        elif str_list.index("l") > str_list.index("r"):
            answer = str_list[str_list.index("r")+1:]
    elif "l" in str_list:  # r이 없는 경우
        answer = str_list[:str_list.index("l")]
    elif "r" in str_list:  # l이 없는 경우
        answer = str_list[str_list.index("r")+1:]
    
    return answer