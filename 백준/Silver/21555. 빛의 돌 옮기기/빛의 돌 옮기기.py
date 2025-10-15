import sys
N, K = map(int, sys.stdin.readline().strip().split())
A = list(map(int, sys.stdin.readline().strip().split()))
B = list(map(int, sys.stdin.readline().strip().split()))
dp = [[0, 0] for _ in range(N)]
dp[0] = [A[0], B[0]]

for i in range(1, N):
    dp[i][0] = min(dp[i - 1][0], dp[i - 1][1] + K) + A[i]
    dp[i][1] = min(dp[i - 1][1], dp[i - 1][0] + K) + B[i]

print(min(dp[-1]))