str = input()

for s in str:
    if s == s.upper(): #비교연산자
        s = s.lower()  #할당연산자
    else:
        s = s.upper()
        
    print(s, end='')
    