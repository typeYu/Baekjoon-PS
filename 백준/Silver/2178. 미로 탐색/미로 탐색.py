from collections import deque
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))
def bfs(x, y):
    count = 1
    queue = deque([(x, y, count)])
    while queue:
        x, y, count = queue.popleft()
        if x == N - 1 and y == M - 1:
            break
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1),]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny, count + 1))
    return count
print(bfs(0, 0))