N = int(input())
graph = [[float('inf')] * N for _ in range(N)]
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    graph[b - 1][a - 1] = 1

for i in range(N):
    graph[i][i] = 0

for k in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(N):
    count = 0
    for j in range(N):
        if graph[i][j] == float('inf') and graph[j][i] == float('inf'):
            count += 1
    print(count)