def solution(arr1, arr2):
    if not arr1 == arr2: # 배열 다름
        if len(arr1) < len(arr2):
            return -1 
        elif len(arr1) > len(arr2):
            return 1
        elif len(arr1) == len(arr2):
            return -1 if sum(arr1)<sum(arr2) else 1 if sum(arr1)>sum(arr2) else 0
    else:
        return 0
            