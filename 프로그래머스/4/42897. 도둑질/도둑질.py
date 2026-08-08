def solution(money):
    dp1, dp2 = [0] * len(money), [0] * len(money)
    for i in range(0, len(money) - 1):
        dp1[i] = max(dp1[i - 2] + money[i], dp1[i - 1])
    
    for i in range(1, len(money)):
        dp2[i] = max(dp2[i - 2] + money[i], dp2[i - 1])
    return max(max(dp1), max(dp2))