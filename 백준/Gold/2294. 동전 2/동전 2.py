import sys
n, k = map(int, sys.stdin.readline().strip().split())
dp = [float('inf')] * (k + 1)
dp[0] = 0
coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline()))

coins.sort()

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

answer = dp[-1]
if answer == float('inf'):
    print(-1)
else:
    print(answer)