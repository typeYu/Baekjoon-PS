# 내가 생각 못한 것
# 1. 다른 배낭문제와 달리 "이상" 도 됨. 그래서 C + 100

import sys
C, N = map(int, sys.stdin.readline().strip().split())
dp = [float('inf')] * (C + 100)
dp[0] = 0
for _ in range(N):
    cost, customer = map(int, sys.stdin.readline().strip().split())
    for i in range(C + 100):
        dp[i] = min(dp[i], dp[i - customer] + cost)

print(min(dp[C:]))