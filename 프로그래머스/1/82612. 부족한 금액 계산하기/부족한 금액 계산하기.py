def solution(price, money, count):
    real_price = 0
    for i in range(1,count+1):
        real_price += price*i
    if real_price - money <= 0:
        return 0
    return real_price - money