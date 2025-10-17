def solution(babbling):
    result =0
    can = ["aya", "ye", "woo", "ma" ]
    
    for ba in babbling:
        for ca in can:
            ba = ba.replace(ca, ' ') #ca를 공백으로 변경
            
        # 공백변경 이후, 문자열 길이가 0인 애들은 result+=1
        if len( ba.strip() ) == 0:
            result +=1 
    return result