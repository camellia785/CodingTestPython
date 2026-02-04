def solution(wallet, bill):
    w_min, w_max = min(wallet), max(wallet)
    answer = 0
    
    # 항상 긴쪽을 접음
    while w_min < min(bill) or w_max < max(bill):
        
        #항상 긴 쪽을 접기
        if bill[0] > bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
            
        answer += 1

    return answer