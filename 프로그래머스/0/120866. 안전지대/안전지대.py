def solution(board):
		# 전체 n, danger set으로 초기화
    n = len(board)
    danger = set()
    
    # i,j 두번을 돌면서 위험 존 가져오기
    # enumerate "좌표와 값을 동시에 꺼내기"
    for i, row in enumerate(board):
        for j, x in enumerate(row):
        
            if not x:
                continue
            danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1, 0, 1])
            
    return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)