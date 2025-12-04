def solution(spell, dic):
    target = ''.join(sorted(spell)) # spell 정렬
    
    for word in dic: # word 돌면서 정렬하려구
        if ''.join(sorted(word)) == target: ## target과 같으면 1
            return 1
        
    return 2