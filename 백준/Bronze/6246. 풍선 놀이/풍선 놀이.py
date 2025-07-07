N, Q = map(int, input().split())
visited = [0] * (N + 1)
for _ in range(Q):
    start, degree = map(int, input().split())
    while start <= N:
        visited[start] = 1
        start += degree
print(visited.count(0) - 1)