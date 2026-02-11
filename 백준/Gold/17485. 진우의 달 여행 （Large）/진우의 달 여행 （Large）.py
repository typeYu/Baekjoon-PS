import sys
N, M = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
dp = [[[float('inf')] * 3 for _ in range(M)] for _ in range(N)]

for m in range(M):
    for d in [0, 1, 2]:
        dp[0][m][d] = graph[0][m]

for i in range(1, N):
    for j in range(M):
        if j > 0:
            dp[i][j][0] = min(dp[i - 1][j - 1][1], dp[i - 1][j - 1][2]) + graph[i][j]

        dp[i][j][1] = min(dp[i - 1][j][0], dp[i - 1][j][2]) + graph[i][j]

        if j < M - 1:
            dp[i][j][2] = min(dp[i - 1][j + 1][0], dp[i - 1][j + 1][1]) + graph[i][j]


answer = float('inf')
for d in dp[-1]:
    answer = min(answer, min(d))
    
print(answer)