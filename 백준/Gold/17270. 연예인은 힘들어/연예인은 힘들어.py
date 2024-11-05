import sys
V, M = map(int, sys.stdin.readline().strip().split())
graph = [[float('inf')] * (V + 1) for _ in range(V + 1)]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    graph[a][b] = min(graph[a][b], c)
    graph[b][a] = min(graph[b][a], c)

J, S = map(int, sys.stdin.readline().strip().split())

for i in range(1, V + 1):
    graph[i][i] = 0

for k in range(1, V + 1):
    for a in range(1, V + 1):
        for b in range(1, V + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

short_path = float('inf')
for i in range(1, V + 1):
    if i == J or i == S:
        continue
    short_path = min(short_path, graph[J][i] + graph[i][S])

answer = []
for i in range(1, V + 1):
    if i != J and i != S:
        if graph[J][i] + graph[i][S] == short_path:
            if graph[J][i] <= graph[i][S]:
                answer.append((graph[J][i], i))
answer.sort()
if len(answer) == 0:
    print(-1)
else:
    print(answer[0][1])
