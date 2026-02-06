def solution(n, m, section):
    answer = 0
    painted_until = 0 # 마지막으로 페인트가 칠해진 지점
    
    for s in section:
        # s ~ s+m-1 구간만큼 칠하는것 반복
        if s > painted_until:
            answer += 1 #롤러 한번 사용
            painted_until = s + m -1 #s부터 m길이만큼 칠함
    
    return answer