def solution(s):
    words = s.split(" ") # 공백기준 자르기
    result = []
    
    for word in words: # 자른 단어들을 돌면서
        new = "" #new라는 문자열 정의하기, 돌때마다 초기화
        
        for i, ch in enumerate(word): # 번호랑 글자 규칙
            if i % 2 == 0:
                new += ch.upper()
            else:
                new += ch.lower()
                
        result.append(new) # 새로운 글자 result라는 리스트에 넣고
    
    return " ".join(result) # 리스트를 공백과 함께 Join