def solution(absolutes, signs):
    answer = []
    for i,a in enumerate(absolutes):
        if signs[i] == True:
            answer.append(a)
        else:
            answer.append(-a)

    return sum(answer)