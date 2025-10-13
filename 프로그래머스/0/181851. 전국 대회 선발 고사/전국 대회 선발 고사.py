def solution(rank, attendance):
    true_rank = []
    for i, r in enumerate(rank):
        if attendance[i]:
            true_rank.append((r, i)) # (등수, 번호) 형태로 저장 -> 번호 필요
    a, b, c = sorted(true_rank)[0][1], sorted(true_rank)[1][1], sorted(true_rank)[2][1] # 상위 3명 번호 꺼내기
    return 10000*a + 100*b + c