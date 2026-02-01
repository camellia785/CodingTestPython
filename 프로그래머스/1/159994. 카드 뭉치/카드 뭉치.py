def solution(cards1, cards2, goal):
    # 각 카드 뭉치에서 지금까지 '몇 장' 사용했는지
    count1 = 0
    count2 = 0
    
    for go in goal:
        if go in cards1:
            # 방금 찾은 단어의 위치(index)가, 
            # 지금까지 사용한 개수(count1)와 똑같아야만 '순서대로' 뽑은 것
            if cards1.index(go) == count1:
                count1 += 1
            else:
                return "No" # 중간에 빼먹었으므로 바로 탈락!
                
        elif go in cards2:
            # cards2 검사
            if cards2.index(go) == count2:
                count2 += 1
            else:
                return "No"
                
        else:
            return "No" # 두 뭉치 어디에도 없는 단어일 경우
            
    return "Yes"