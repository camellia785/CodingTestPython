def solution(answers):
    result = []
    score_list = [0] * 4 #미리 채워둬야 활용 가능
    
    num_1 = [1,2,3,4,5] * ((len(answers)//5)+1)
    num_2 = [2,1,2,3,2,4,2,5] * ((len(answers)//8)+1)
    num_3 = [3,3,1,1,2,2,4,4,5,5] * ((len(answers)//10)+1)
    
    # 점수계산
    for i, answer in enumerate(answers):
        if num_1[i] == answer:
            score_list[1] += 1
        
        if num_2[i] == answer:
            score_list[2] += 1
    
        if num_3[i] == answer:
            score_list[3] += 1
            
    # 1등찾기
    max_score = max(score_list)
    for i, val in enumerate(score_list):
        if val == max_score:
            result.append(i)
    
    return result