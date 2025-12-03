def solution(board):
    # 문제전략
    # 1전체지도를 보면서 1찾기
    # 2지뢰 발견시 주변 8칸의 좌표저장
    # 3set을 이용해서 주변8칸의 좌표 중복제거저장
    # 4전체칸-위험칸 = 안전한칸 구하기
    n = len(board) # 전체칸
    danger = set() # 위험 지역 좌표를 저장할 집합
    
    # 1전체 보드 돌기 -> 지뢰 1 찾기
    # x와 y에 각각 -1부터 1까지 더해보는 2중 반복문으 돌리면,
    # 자기 자신을 포함한 9칸 한꺼번에 검사 가능
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                
                # 2지뢰 중심으로 주변 위험지역 등록
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        ni = i + dx
                        nj = j + dy
                        
                        # 3지도 밖으로 나가는지 체크
                        if 0 <= ni < n and 0 <= nj < n:
                            danger.add((ni, nj))
                            
    # 4전체칸 - 위험칸 = 안전칸
    return (n*n) - len(danger)