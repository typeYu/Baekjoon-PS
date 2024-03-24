from collections import deque
T = int(input())
def bfs(x, y):
    queue = deque([(x, y)])
    graph[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0

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