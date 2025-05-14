import sys
from collections import deque
N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
max_height = 0
min_height = float('inf')


def bfs(y, x, height):
    queue = deque([(y, x)])
    visited[y][x] = True

    while queue:
        y, x = queue.popleft()
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and graph[ny][nx] > height:
                queue.append((ny, nx))
                visited[ny][nx] = True


answer = 0
for height in range(0, 101):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j] > height:
                bfs(i, j, height)
                cnt += 1

    answer = max(answer, cnt)

print(answer)