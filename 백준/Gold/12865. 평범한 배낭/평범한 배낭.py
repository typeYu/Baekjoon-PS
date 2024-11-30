import sys
N, K = map(int, sys.stdin.readline().strip().split())
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    W, V = map(int, sys.stdin.readline().strip().split())
    for j in range(1, K + 1):
        if j < W:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        else:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - W] + V, dp[i - 1][j])

print(dp[N][K])