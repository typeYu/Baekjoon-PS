import sys
from collections import deque
N, M, K = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

def bfs(D):
    count = 0

    visited = [[False] * M for _ in range(N)]
    queue = deque()

    # 조건에 맞다면 테두리 중 왼쪽, 오른쪽을 큐에 넣음
    for i in range(N):
        if graph[i][0] <= D:
            queue.append((i, 0))
            visited[i][0] = True
            count += 1
        if graph[i][M - 1] <= D:
            queue.append((i, M - 1))
            visited[i][M - 1] = True
            count += 1

    # 테두리 중 윗부분을 큐에 넣음
    for j in range(1, M - 2):
        if graph[0][j] <= D:
            queue.append((0, j))
            visited[0][j] = True
            count += 1

    while queue:
        y, x = queue.popleft()
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and graph[ny][nx] <= D:
                visited[ny][nx] = True
                queue.append((ny, nx))
                count += 1

    return count

def binary_search():
    start, end = 1, max(max(graph[i]) for i in range(N))
    while start <= end:
        mid = (start + end) // 2

        bfs_result = bfs(mid)
        if bfs_result < K:
            start = mid + 1
        else:
            end = mid - 1

    return start

print(binary_search())