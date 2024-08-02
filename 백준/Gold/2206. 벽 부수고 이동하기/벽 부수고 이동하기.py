from collections import deque
N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[[0, 0] for _ in range(M)] for _ in range(N)] # 3차원 배열, 벽 부쉈으면 visited[][][1]


def bfs(i, j, k):
    queue = deque([(i, j, k)])
    visited[i][j][k] = 1

    while queue:
        y, x, destroy = queue.popleft()
        if y == (N - 1) and x == (M - 1):
            return visited[y][x][destroy]
        for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                # 만약 그래프 상으로 0이고 방문 안했으면
                if graph[ny][nx] == 0 and visited[ny][nx][destroy] == 0:
                    queue.append((ny, nx, destroy))
                    visited[ny][nx][destroy] = visited[y][x][destroy] + 1
                # 만약 그래프 상으로 1이고 아직 파괴 안했고 3차원 배열의 z축으로 방문 안했으면
                elif graph[ny][nx] == 1 and destroy == 0 and visited[ny][nx][1] == 0:
                    queue.append((ny, nx, destroy + 1))
                    visited[ny][nx][destroy + 1] = visited[y][x][destroy] + 1
    return -1


print(bfs(0, 0, 0))
