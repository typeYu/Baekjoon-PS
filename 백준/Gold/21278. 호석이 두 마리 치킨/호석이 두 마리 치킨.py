from itertools import combinations
N, M = map(int, input().split())
graph = [[float('inf')] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, N + 1):
    graph[i][i] = 0

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

comb = combinations([i for i in range(1, N + 1)], 2)

time, num = float('inf'), []
for c1, c2 in comb:
    total = 0
    for i in range(1, N + 1):
        total += min(graph[c1][i], graph[c2][i]) * 2
    if total < time:
        time = total
        num = [c1, c2]

print(*num, end=' ')
print(time)