import sys
N, M = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] + graph[i - 1][j - 1] - dp[i - 1][j - 1]

for _ in range(int(sys.stdin.readline())):
    y1, x1, y2, x2 = map(int, sys.stdin.readline().strip().split())
    print(dp[y2][x2] - dp[y2][x1 - 1] - dp[y1 - 1][x2] + dp[y1 - 1][x1 - 1])