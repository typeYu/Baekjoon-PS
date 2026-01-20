import sys
N, M = map(int, sys.stdin.readline().strip().split())
graph = [[float('inf')] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b, t = map(int, sys.stdin.readline().strip().split())
    graph[a][b] = min(graph[a][b], t)

K = int(sys.stdin.readline())
C = list(map(int, sys.stdin.readline().strip().split()))

for i in range(1, N + 1):
    graph[i][i] = 0

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = float('inf')
arr = []

for city in range(1, N + 1):
    ans = 0
    ok = True

    for friend in C:
        if graph[friend][city] == float('inf') or graph[city][friend] == float('inf'):
            ok = False
            break
        ans = max(ans, graph[friend][city] + graph[city][friend])

    if not ok:
        continue

    if answer > ans:
        answer = ans
        arr = [city]
    elif answer == ans:
        arr.append(city)

print(*arr)
