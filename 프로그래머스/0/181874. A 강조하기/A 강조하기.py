def solution(myString):
    return ''.join(
        "A" if s=="a" else s.lower() if s != "A" else s for s in myString)