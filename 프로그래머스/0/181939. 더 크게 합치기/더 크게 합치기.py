def solution(a, b):
    a, b = str(a), str(b)
    return max( int(a+b), int(b+a) )

# f 포멧으로 더 간단하게 하기
def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))
