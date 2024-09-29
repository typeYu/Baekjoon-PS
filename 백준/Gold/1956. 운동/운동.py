import sys
N, M = map(int, sys.stdin.readline().strip().split())
graph = [[float('inf')] * N for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    graph[a - 1][b - 1] = c

for i in range(N):
    graph[i][i] = 0

for k in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = float('inf')
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        else:
            result = min(result, graph[i][j] + graph[j][i])

if result == float('inf'):
    print(-1)
else:
    print(result)