N, K = map(int, input().split())
dp = [1] * (N + 1)

for k in range(1, K):
    for n in range(1, N + 1):
        dp[n] += dp[n - 1]

print(dp[-1] % 1000000000)