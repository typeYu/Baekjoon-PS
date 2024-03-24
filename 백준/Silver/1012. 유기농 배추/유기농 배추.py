from collections import deque
T = int(input())
def bfs(y, x):
    queue = deque([(y, x)])
    graph[y][x] = 0
    while queue:
        y, x = queue.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 1:
                queue.append((ny, nx))
                graph[ny][nx] = 0

while T:
    M, N, K = map(int, input().split())
    graph = [[0] * M for i in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        graph[b][a] = 1
    count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i, j)
                count += 1
    print(count)
    T -= 1