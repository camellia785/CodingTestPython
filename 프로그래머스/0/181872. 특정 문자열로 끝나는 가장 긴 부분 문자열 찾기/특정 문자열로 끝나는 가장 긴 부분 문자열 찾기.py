def solution(myString, pat):
    n, m = len(myString), len(pat)
    # pat이 온전히 들어갈 수 있는 뒤에서부터 앞으로 거슬러가기
    for i in range(n-m, -1, -1):
        if myString[i:i+m] == pat:
            return myString[:i+m]