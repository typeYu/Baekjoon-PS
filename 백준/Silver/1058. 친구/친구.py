import sys
N = int(sys.stdin.readline())
array = [list(sys.stdin.readline().strip()) for _ in range(N)]
graph = []
max_cnt = 0

for arr in array:
    new = []
    for a in arr:
        if a == 'Y':
            new.append(1)
        else:
            new.append(float('inf'))
    graph.append(new)

for i in range(N):
    graph[i][i] = 0

for k in range(N):
    for y in range(N):
        for x in range(N):
            graph[y][x] = min(graph[y][x], graph[y][k] + graph[k][x])

answer = 0
for g in graph:
    answer = max(answer, g.count(1) + g.count(2))

print(answer)