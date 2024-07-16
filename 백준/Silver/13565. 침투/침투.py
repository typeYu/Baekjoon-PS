from collections import deque
M, N = map(int, input().split()) # 세로, 가로
graph = [list(map(int, input())) for _ in range(M)]
visited = [[False] * N for _ in range(M)]


def bfs(y, x):
    queue = deque([(y, x)])
    visited[y][x] = True
    graph[y][x] = 3 # 전류

    while queue:
        y, x = queue.popleft()
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < M and 0 <= nx < N and graph[ny][nx] == 0 and not visited[ny][nx]:
                queue.append((ny, nx))
                graph[ny][nx] = 3
                visited[ny][nx] = True


for i in range(N):
    if graph[0][i] == 0:
        bfs(0, i)

for j in range(N):
    if graph[M - 1][j] == 3:
        print("YES")
        exit()
print("NO")