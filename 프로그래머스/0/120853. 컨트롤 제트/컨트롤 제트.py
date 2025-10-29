def solution(s):
    stack = []
    for x in s.split():
        if x == "Z":
            if stack: #비어있지 않은경우 pop
                stack.pop()
        else:
            stack.append(int(x))
    return sum(stack)