from collections import deque
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = [[False] * m for _ in range(n)]

def bfs(x, y):
    queue = deque([(x, y)])
    if not visited[x][y]:
        graph[x][y] = 0
        visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
                queue.append((nx, ny)) # 큐에 방문한 좌표 넣어줘야
                graph[nx][ny] = graph[x][y] + 1
                visited[nx][ny] = True

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            graph[i][j] = -1

for row in graph:
    print(' '.join(map(str, row)))