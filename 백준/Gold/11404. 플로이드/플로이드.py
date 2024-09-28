import sys
n = int(sys.stdin.readline())
graph = [[float('inf')] * n for _ in range(n)]
for _ in range(int(sys.stdin.readline())):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    graph[a - 1][b - 1] = min(graph[a - 1][b - 1], c) # 도시 a에서 b로 가는 버스가 여러 개 있음

for i in range(n):
    graph[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(n):
    for j in range(n):
        if graph[i][j] == float('inf'):
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()