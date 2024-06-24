from collections import deque
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
visited = [[False] * N for _ in range(M)]


def bfs(y, x):
    queue = deque([(y, x)])
    visited[y][x] = True
    while queue:
        y, x = queue.popleft()
        for dy, dx in [(1, 0), (0, 1)]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < M and 0 <= nx < N and graph[ny][nx] == 1 and not visited[ny][nx]:
                queue.append((ny, nx))
                visited[ny][nx] = True

    if visited[M - 1][N - 1]:
        return "Yes"
    else:
        return "No"


print(bfs(0, 0))