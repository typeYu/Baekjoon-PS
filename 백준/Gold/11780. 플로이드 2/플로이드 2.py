import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]
record = [[float('inf')] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)
    record[a][b] = a

for i in range(1, n + 1):
    graph[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                record[i][j] = record[k][j]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        print(0 if graph[a][b] == float('inf') else graph[a][b], end=' ')
    print()

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j or record[i][j] == float('inf'):
            print(0)
            continue

        answer = [j]
        node = j
        while record[i][node] != float('inf'):
            nxt = record[i][node]
            answer.append(nxt)
            node = nxt
        print(len(answer), end=' ')
        print(*answer[::-1])