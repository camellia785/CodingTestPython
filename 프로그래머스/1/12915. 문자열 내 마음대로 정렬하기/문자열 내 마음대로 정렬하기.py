def solution(strings, n):
    def sort_logic(word):
        return (word[n], word) # (기준1, 기준2) 튜플형태 반환
    
    strings.sort(key=sort_logic)
    
    return strings

# 방법2 -> 함수 두개 정의하는 것 대신에, 일회용함수 람다 사용
# def solution(strings, n):
#     # sort_logic 함수 자리에 람다를 직접 집어넣기
#     strings.sort(key=lambda x: (x[n], x))
#     return strings