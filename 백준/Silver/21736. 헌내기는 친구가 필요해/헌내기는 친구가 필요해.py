from collections import deque
N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

def bfs(x, y):
    countP = 0
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] != "X":
                queue.append((nx, ny))
                visited[nx][ny] = True
                if graph[nx][ny] == "P":
                    countP += 1
    if countP == 0:
        return "TT"
    else:
        return countP

for i in range(N):
    for j in range(M):
        if graph[i][j] == "I":
            print(bfs(i, j))
            break