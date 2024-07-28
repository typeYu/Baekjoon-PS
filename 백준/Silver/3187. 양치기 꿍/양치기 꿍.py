from collections import deque
R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
v, k = 0, 0

def bfs(y, x):
    global v, k
    sheep, wolf = 0, 0
    queue = deque([(y, x)])
    visited[y][x] = True

    while queue:
        y, x = queue.popleft()
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < R and 0 <= nx < C and not visited[ny][nx] and graph[ny][nx] != '#':
                queue.append((ny, nx))
                visited[ny][nx] = True
                if graph[ny][nx] == 'v':
                    wolf += 1
                elif graph[ny][nx] == 'k':
                    sheep += 1

    if wolf < sheep:
        k += sheep
    else:
        v += wolf

for i in range(R):
    for j in range(C):
        if not visited[i][j]:
            bfs(i, j)

print(k, v)