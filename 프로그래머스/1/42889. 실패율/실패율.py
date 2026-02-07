def solution(N, stages):
    answer = []
    people = len(stages)
    percent = [] # (실패율, 스테이지번호) 2차원으로 넣기
    
    # stages.count(i) 대체 -> cnt 한번만 세기
    count = [0] * (N+2) # 인덱스 0부터 시작하니까 N+1개의 숫자 넣기 용이
    for s in stages:
        count[s] += 1
    
    # 1. 실패율 계산하기
    for i in range(1,N+1):
        if people != 0:
            percent.append((count[i] / people, i)) # (실패율, 스테이지번호)
            people -= count[i]
        else:
            percent.append((0,i)) # people이 0이면, 0 퍼센트로 넣기
        
    print(percent)
    
    # 2. 실패율 기준 내림차순 -> 실패율 큰거부터 나오게
    percent.sort(key=lambda x: (-x[0], x[1]))
    
    print(percent)
    
    # 3. 스테이지 번호만 나오게
    for p in percent:
        answer.append(p[1])

    return answer