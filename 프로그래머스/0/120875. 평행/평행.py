def solution(dots): 
    # 두 직선이 평행하려면 기울기가 같아야함
    # (y2-y1) / (x2-x1)
    # dots[0], dots[1], dots[2], dots[3]
    
    # 1. 점 P1-P2를 잇는 직선과 점 P3-P4를 잇는 직선의 기울기 비교
    # P1: dots[0], P2: dots[1], P3: dots[2], P4: dots[3]
    if (dots[1][1] - dots[0][1]) * (dots[3][0] - dots[2][0]) == (dots[3][1] - dots[2][1]) * (dots[1][0] - dots[0][0]):
        return 1
        
    # 2. 점 P1-P3를 잇는 직선과 점 P2-P4를 잇는 직선의 기울기 비교
    # P1: dots[0], P3: dots[2], P2: dots[1], P4: dots[3]
    if (dots[2][1] - dots[0][1]) * (dots[3][0] - dots[1][0]) == (dots[3][1] - dots[1][1]) * (dots[2][0] - dots[0][0]):
        return 1
        
    # 3. 점 P1-P4를 잇는 직선과 점 P2-P3를 잇는 직선의 기울기 비교
    # P1: dots[0], P4: dots[3], P2: dots[1], P3: dots[2]
    if (dots[3][1] - dots[0][1]) * (dots[2][0] - dots[1][0]) == (dots[2][1] - dots[1][1]) * (dots[3][0] - dots[0][0]):
        return 1
    
    return 0