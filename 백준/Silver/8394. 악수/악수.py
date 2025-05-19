# 한 명: 1
# 두 명: 2
# 세 명: 3
# 네 명: 5
# 다섯 명: 8
# 여섯 명: 13

import sys
n = int(sys.stdin.readline())
dp = [1] * (n + 1)
dp[1] = 1
dp[2] = 2

if n > 2:
    for i in range(3, n + 1):
        dp[i] = ((dp[i - 1] % 10) + (dp[i - 2] % 10)) % 10

print(dp[-1])
