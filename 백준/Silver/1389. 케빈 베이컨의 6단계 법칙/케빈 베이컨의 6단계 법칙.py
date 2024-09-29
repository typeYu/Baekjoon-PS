import sys
N, M = map(int, sys.stdin.readline().strip().split())
graph = [[float('inf')] * N for _ in range(N)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1

for i in range(N):
    graph[i][i] = 0

for k in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

min_result = float('inf')
result = 0
for i in range(len(graph)):
    if min_result > sum(graph[i]):
        result = i + 1
        min_result = sum(graph[i])

print(result)