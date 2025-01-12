import sys
n, k = map(int, sys.stdin.readline().strip().split())
coins = []
dp = [0] * (k + 1)
dp[0] = 1

for i in range(n):
    coin = int(sys.stdin.readline())
    coins.append(coin)

for coin in coins:
    for i in range(coin, k + 1): # dp[i - coin] 값이 -가 나오며 안되므로 coin부터
        dp[i] = dp[i] + dp[i - coin]
print(dp[-1])