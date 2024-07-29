from collections import deque
from copy import deepcopy
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
result = 0

def make_wall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(cnt + 1)
                graph[i][j] = 0


def bfs():
    copy_graph = deepcopy(graph)
    visited = [[False] * M for _ in range(N)]
    queue = deque()

    for i in range(N):
        for j in range(M):
            if copy_graph[i][j] == 2:
                queue.append((i, j))
                visited[i][j] = True

    while queue:
        y, x = queue.popleft()
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and copy_graph[ny][nx] != 1:
                queue.append((ny, nx))
                copy_graph[ny][nx] = 2
                visited[ny][nx] = True

    global result
    safe_zone = 0
    for i in range(N):
        for j in range(M):
            if copy_graph[i][j] == 0:
                safe_zone += 1
    result = max(result, safe_zone)

make_wall(0)
print(result)
