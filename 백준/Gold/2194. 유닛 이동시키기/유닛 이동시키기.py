from collections import deque
N, M, A, B, K = map(int, input().split())
graph = [[0] * M for _ in range(N)]
for _ in range(K):
    i, j = map(int, input().split())
    graph[i - 1][j - 1] = -1 # 장애물
start_i, start_j = map(int, input().split())
end_i, end_j = map(int, input().split())


def obstacle(ny, nx):
    for i in range(A):
        for j in range(B):
            if ny + i >= N or nx + j >= M or graph[ny + i][nx + j] == -1:
                return False
    return True


def bfs(i, j):
    result = 0
    visited = [[False] * M for _ in range(N)]
    queue = deque([(i, j, result)])
    visited[i][j] = True

    while queue:
        y, x, result = queue.popleft()
        if y == end_i - 1 and x == end_j - 1:
            return result
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and obstacle(ny, nx):
                queue.append((ny, nx, result + 1))
                visited[ny][nx] = True
    return -1


print(bfs(start_i - 1, start_j - 1))