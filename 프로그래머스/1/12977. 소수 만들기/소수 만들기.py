def solution(nums):
    answer = [] # 합 리스트
    result = 0 # 소수가 되는 합의 개수, 정답
    
    # ‼️ nC3 구하기
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                answer.append(nums[i]+nums[j]+nums[k])

    for a in answer:
        count = 0 # 한 a의 약수 개수들
        
        # ‼️ 소수가 되는 경우 구하기
        for b in range(1, int(a**(0.5))+1):
            if a % b == 0:
                if a*a == b:
                    count +=1
                else:
                    count += 2
        
        if count == 2:
            result +=1

    return result