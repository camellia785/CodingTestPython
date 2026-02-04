def solution(a, b):
    # 1. 각 월의 일수를 리스트로 저장 
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # 2. 요일 이름 리스트 -> 1월 1일이 FRI이므로 인덱스1이 FRI, 7나눈 나머지
    days = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    
    # 3. total_days 구하기
    total_days = sum(months[:a-1]) + b
    
    return days[total_days % 7]