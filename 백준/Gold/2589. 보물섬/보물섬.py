from collections import deque
N, M = map(int, input().split())
graph = [list(map(str, input())) for _ in range(N)]

land_index = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'L':
            land_index.append((i, j))

def bfs():
    max_move = 0
    for i, j in land_index:
        visited = [[-1] * M for _ in range(N)]
        count = 0
        queue = deque([(i, j, count)])
        visited[i][j] = count

        while queue:
            y, x, count = queue.popleft()
            max_move = max(max_move, count)
            for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] == 'L' and visited[ny][nx] == -1:
                    visited[ny][nx] = count + 1
                    queue.append((ny, nx, count + 1))

    return max_move

print(bfs())





