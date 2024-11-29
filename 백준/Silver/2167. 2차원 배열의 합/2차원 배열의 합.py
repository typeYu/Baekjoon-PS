import sys
N, M = map(int, sys.stdin.readline().strip().split())
graph = [[0] + list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
graph.insert(0, [0] * (M + 1))
for i in range(1, N + 1):
    for j in range(1, M + 1):
        graph[i][j] = graph[i][j] + graph[i - 1][j] + graph[i][j - 1] - graph[i - 1][j - 1]

for _ in range(int(sys.stdin.readline())):
    i, j, y, x = map(int, sys.stdin.readline().strip().split())
    print(graph[y][x] - graph[i - 1][x] - graph[y][j - 1] + graph[i - 1][j - 1])