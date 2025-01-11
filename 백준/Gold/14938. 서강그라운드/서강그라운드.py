import sys
n, m, r = map(int, sys.stdin.readline().strip().split())
t = [0] + list(map(int, sys.stdin.readline().strip().split()))
graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]
for _ in range(r):
    a, b, l = map(int, sys.stdin.readline().strip().split())
    graph[a][b] = min(graph[a][b], l)
    graph[b][a] = min(graph[b][a], l)

for i in range(1, n + 1):
    graph[i][i] = 0

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

max_item = 0
for i in range(1, n + 1):
    total = 0
    for j in range(1, n + 1):
        if graph[i][j] <= m:
            total += t[j]
    max_item = max(max_item, total)

print(max_item)