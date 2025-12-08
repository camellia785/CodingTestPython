def solution(id_pw, db):
    userId, userPw = id_pw # 분리
    
    # db확인
    for dbId, dbPw in db:
        if dbId == userId:
            if dbPw == userPw:
                return "login"
            else:
                return "wrong pw"
            
    return "fail"