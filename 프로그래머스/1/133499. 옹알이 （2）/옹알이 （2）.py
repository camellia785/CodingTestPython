def solution(babbling):
    answer = 0
    sounds = ["aya", "ye", "woo", "ma" ]
    
    for bab in babbling:
        valid = True #초기화
        
        # 1) 같은 발음이 연속되면 탈락
        for s in sounds:
            if s*2 in bab:
                valid = False
                break
        
        if not valid:
            continue # valid가 True인 경우만
        
        # 2) 허용된 발음을 공백으로 치환 -> ""이면 발음가능
        temp = bab # temp에 bab 임시저장
        for s in sounds:
            temp = temp.replace(s, " ")
            
        if temp.strip() == "":
            answer += 1

    return answer