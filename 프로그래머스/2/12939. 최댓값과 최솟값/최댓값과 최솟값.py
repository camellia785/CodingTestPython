def solution(s):
    mylist = list(map(int, s.split()))
    answer = str(min(mylist)) +' '+ str(max(mylist))
    return answer