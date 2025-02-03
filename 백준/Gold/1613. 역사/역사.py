import sys
n, k = map(int, sys.stdin.readline().strip().split())
graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]

for _ in range(k):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a][b] = 1

for i in range(1, n + 1):
    graph[i][i] = 0

for k in range(n + 1):
    for a in range(n + 1):
        for b in range(n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# graph[i][j]의 값이 INF가 아니라는 것은 i 가 j보다 먼저 일어났다는 것이다.
# 또한 graph[i][j]가 INF이고 graph[j][i]가 INF가 아니라면 j가 i보다 먼저 일어났다는 것이다.
# 둘 다 INF라면 알 수 없다는 뜻이다.(연결되지 않았으므로)
for _ in range(int(sys.stdin.readline())):
    first, end = map(int, sys.stdin.readline().strip().split())
    if graph[first][end] < float('inf'):
        print(-1)
    elif graph[end][first] < float('inf'):
        print(1)
    else:
        print(0)