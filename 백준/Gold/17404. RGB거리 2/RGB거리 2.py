N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
answer = float('inf')

for i in range(3):
    dp = [[float('inf'), float('inf'), float('inf') ] for _ in range(N)]
    dp[0][i] = graph[0][i]

    for j in range(1, N):
        for k in range(3):
            dp[j][k] = graph[j][k] + min(dp[j - 1][(k + 1) % 3], dp[j - 1][(k + 2) % 3])

    for j in range(3):
        if i != j:
            answer = min(answer, dp[-1][j])

print(answer)