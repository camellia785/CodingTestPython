str = input()

for s in str:
    if s == s.upper(): #비교연산자
        s = s.lower()  #할당연산자
    else:
        s = s.upper()
        
    print(s, end='')

# ‼️ 다른사람 풀이 - swapcase()라는 대소문자 변환 함수 존재
# print(input().swapcase())
