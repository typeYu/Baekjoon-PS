# 항상 동쪽이나 남쪽으로 이동해야 하므로, max(dp[i - 1][j], dp[i][j - 1])이고, 지금까지 마신 우유 개수에서 이번에 먹어야 하는 우유 종류 추출 후 해당 된다면 +1
# %3: 다음에 마셔야 할 우유의 종류. 이전까지 먹었던 우유가 1개라면 이번에 먹어야 할 우유는 1, 이저까지 먹었던 우유가 2개이면 이번에 먹어야 하는 우유는 2..
import sys
N = int((sys.stdin.readline().strip()))
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

# 시작점 (0,0)
dp[0][0] = 1 if graph[0][0] == 0 else 0

# 첫 번째 행, 열 처리
for i in range(1, N):
    dp[i][0] = dp[i - 1][0]
    if graph[i][0] == dp[i][0] % 3:
        dp[i][0] += 1

    dp[0][i] = dp[0][i - 1]
    if graph[0][i] == dp[0][i] % 3:
        dp[0][i] += 1

# 나머지 셀 처리
for i in range(1, N):
    for j in range(1, N):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        if graph[i][j] == dp[i][j] % 3:
            dp[i][j] += 1

print(dp[N - 1][N - 1])