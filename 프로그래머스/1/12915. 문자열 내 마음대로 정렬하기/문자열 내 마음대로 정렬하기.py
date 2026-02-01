def solution(strings, n):
    def sort_logic(word):
        return (word[n], word) # (기준1, 기준2) 튜플형태 반환
    
    strings.sort(key=sort_logic)
    
    return strings