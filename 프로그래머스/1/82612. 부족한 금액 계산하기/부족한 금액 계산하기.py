def solution(price, money, count):
    priceSum = 0
    while count > 0:
        priceSum += price * count
        count -= 1
    if priceSum - money <= 0:
        return 0
    else:
        return priceSum - money