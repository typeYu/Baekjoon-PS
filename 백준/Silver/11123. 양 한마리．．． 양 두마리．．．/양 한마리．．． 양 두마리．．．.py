from collections import deque
T = int(input())

def bfs(x, y):
    count = 0
    queue = deque([(x, y)])
    graph[x][y] = 'C' #complete
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and graph[nx][ny] == '#':
                queue.append((nx, ny))
                graph[nx][ny] = 'C'

for _ in range(T):
    result = 0
    H, W = map(int, input().split())
    graph = [list(input()) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if graph[i][j] == '#':
                bfs(i, j)
                result += 1
    print(result)