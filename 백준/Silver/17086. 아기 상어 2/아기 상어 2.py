from collections import deque
N, M = map(int, input().split()) #세로, 가로
graph = [list(map(int, input().split())) for _ in range(N)]
safe = [] # 상어 인덱스 저장

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            safe.append([i, j])

def bfs(safe):
    visited = [[False] * M for _ in range(N)]
    queue = deque([])
    for y, x in safe:
        queue.append((y, x, 0))
        visited[y][x] = True
    while queue:
        y, x, short_path = queue.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            ny, nx = y + dy, x + dx
            if 0 <= nx < M and 0 <= ny < N and [ny, nx] not in safe and not visited[ny][nx]:
                queue.append((ny, nx, short_path + 1))
                visited[ny][nx] = True
                if graph[ny][nx] == 0:
                    graph[ny][nx] = short_path + 1
                else:
                    min(graph[ny][nx], short_path + 1)

    result = 1
    for i in graph:
        for j in i:
            result = max(j, result)
    return result

print(bfs(safe))