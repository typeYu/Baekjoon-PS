import sys
N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        num = graph[i][j]
        if num == 0:
            continue
        if 0 <= i + num < N:
            dp[i + num][j] += dp[i][j]
        if 0 <= j + num < N:
            dp[i][j + num] += dp[i][j]

print(dp[-1][-1])