def solution(hp):
    jang = hp // 5
    bung = (hp % 5) // 3
    ill = (hp % 5) % 3

    return jang+bung+ill