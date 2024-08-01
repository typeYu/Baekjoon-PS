from collections import deque
N, M = map(int, input().split())
RGB = [list(map(int, input().split())) for _ in range(N)]
T = int(input())
new = [[] for _ in range(N)]

for i in range(N):
    for j in range(0, (M * 3), 3):
        sumRGB = sum(RGB[i][j:j + 3])
        if sumRGB >= T * 3:
            new[i].append(255)
        else:
            new[i].append(0)

visited = [[False] * M for _ in range(N)]


def bfs(y, x):
    queue = deque([(y, x)])
    visited[y][x] = True

    while queue:
        y, x = queue.popleft()
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and new[ny][nx] == 255:
                visited[ny][nx] = True
                queue.append((ny, nx))


count = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j] and new[i][j] == 255:
            bfs(i, j)
            count += 1

print(count)