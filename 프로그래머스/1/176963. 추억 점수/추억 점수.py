def solution(name, yearning, photo):
    answer = []
    for p in photo:
        temp = 0
        for person in p:
            if person in name:
                temp += yearning[name.index(person)]
        answer.append(temp)

    return answer