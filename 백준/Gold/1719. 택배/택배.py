import sys
n, m = map(int, sys.stdin.readline().strip().split())
graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]
record = [[float('inf')] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    graph[a][b] = c
    graph[b][a] = c
    record[a][b] = b
    record[b][a] = a

for i in range(1, n + 1):
    graph[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                record[i][j] = record[i][k]

for i in range(1, n + 1):
    for j in record[i][1:]:
        if j == float('inf'):
            print('-', end=' ')
        else:
            print(j, end=' ')
    print()