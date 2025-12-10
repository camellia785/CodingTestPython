def solution(A, B):
    # 처음부터 같은경우
    if A == B:
        return 0
    
    # 문자열 길이만큼 밀어보기
    for cnt in range(1, len(A)+1):
        # 오른쪽 한칸밀기
        A = A[-1] + A[:-1]
        
        # 밀고 같으면, 횟수 반환
        if A == B:
            return cnt
    
    # 끝까지 없으면 불가능
    return -1