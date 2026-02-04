def solution(number, limit, power):
    total_iron = 0
    
    for i in range(1, number+1):
        count = 0
        # 1. 공격력(약수개수) 구하는 for: 루트 n까지만 하면 +2개씩
        for j in range(1, int(i**0.5)+1 ):
            if i % j == 0:
                if j*j == i:
                    count += 1
                else:
                    count += 2
            
            # 1-2. 계산 중간에 limit을 넘었다면, break (최적화)
            if count > limit:
                break
                
        # 2. limit 체크 후, 철무게 합산해가기
        if count > limit:
            total_iron += power
        else:
            total_iron += count
            
    return total_iron