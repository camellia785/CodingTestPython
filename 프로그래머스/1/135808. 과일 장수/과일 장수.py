def solution(k, m, score):
    answer = 0
    score.sort(reverse=True) # [4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1]
    
    # m=3일경우 인덱스 0,1,2(이거) 끊고 3,4,5(이거) 끊고 6,7,8(이거) 끊음 [m-1, 2m-1, 3m-1]
    for i in range(m-1, len(score), m): # i 로 필요한건 최솟값이 나오는 인덱스
        answer += score[i]*m
    
    
    return answer