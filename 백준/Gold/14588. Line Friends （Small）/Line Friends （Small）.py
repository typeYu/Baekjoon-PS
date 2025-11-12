import sys

def floyd():
    for i in range(1, N + 1):
        graph[i][i] = 0

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                continue
            l1, r1 = location[i][0], location[i][1]
            l2, r2 = location[j][0], location[j][1]

            if (l1 > r2) or (r1 < l2):
                continue
            else:
                graph[i][j] = 1
                graph[j][i] = 1

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if graph[i][k] + graph[k][j] != float('inf'):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


N = int(sys.stdin.readline())

location = [[float('inf'), float('inf')]]
for _ in range(N):
    l, r = map(int, sys.stdin.readline().strip().split())
    location.append([l, r])

graph = [[float('inf')] * (N + 1) for _ in range(N + 1)]
floyd()

Q = int(sys.stdin.readline())
for _ in range(Q):
    a, b = map(int, sys.stdin.readline().strip().split())
    print(graph[a][b] if graph[a][b] != float('inf') else -1)