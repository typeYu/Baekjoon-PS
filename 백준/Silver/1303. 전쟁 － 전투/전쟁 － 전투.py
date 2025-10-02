import sys
from collections import deque


def bfs(y, x, S):
    global white, blue, visited
    queue = deque([(y, x)])
    visited[y][x] = True
    cnt = 1

    while queue:
        y, x = queue.popleft()
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < M and 0 <= nx < N and not visited[ny][nx] and graph[ny][nx] == S:
                visited[ny][nx] = True
                queue.append((ny, nx))
                cnt += 1

    if S == 'W':
        white += cnt ** 2
    else:
        blue += cnt ** 2


N, M = map(int, sys.stdin.readline().strip().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(M)]
visited = [[False] * N for _ in range(M)]
white, blue = 0, 0

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, graph[i][j])


print(white, blue)