def solution(arr):
    
    num_rows = len(arr)
    num_cols = len(arr[0])
    
    if num_rows > num_cols:
        # 각 행의 길이에 0을 추가
        zeros_to_add = num_rows - num_cols
        for row in arr:
            row.extend([0]* zeros_to_add) # row에 원소 추가할 때 extend
            
    elif num_cols > num_rows:
        # 0으로 채워진 행을 추가
        rows_to_add = num_cols - num_rows
        zero_row = [0] * num_cols
        for _ in range(rows_to_add):
            arr.append(zero_row)
            
    return arr