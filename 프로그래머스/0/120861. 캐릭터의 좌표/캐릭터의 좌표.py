def solution(keyinput, board):
    x, y = 0,0 # 시작점
    
    # 이동 가능한 최대 범위
    max_x = board[0] // 2 # 소수점 버림
    max_y = board[1] // 2
    
    
    for key in keyinput:
        if key == "left":
            if x -1 >= -max_x:
                x -= 1
        elif key == "right":
            if x+1 <= max_x:
                x += 1
                
        elif key == "up":
            if y+1 <= max_y:
                y += 1
        elif key == "down":
            if y-1 >= -max_y:
                y -= 1
            
    return [x,y]