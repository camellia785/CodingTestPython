def solution(s, n):
    answer = ''
    letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # 0~25까지 26개
    lower_letter = letter.lower()
    
    for word in s:
        if word in letter: #대문자의경우
            word = letter[(letter.index(word) + n) % 26]
            answer += word

        elif word in lower_letter: #소문자의 경우
            word = lower_letter[(lower_letter.index(word) + n) % 26]
            answer += word
        
        else: #공백일경우 그냥추가
            answer += word
    
    return answer