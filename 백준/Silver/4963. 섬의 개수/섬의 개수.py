from collections import deque

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    def bfs(y, x):
        queue = deque([(y, x)])
        visited[y][x] = True

        while queue:
            y, x = queue.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < w and 0 <= ny < h and graph[ny][nx] == 1 and visited[ny][nx] == False:
                    graph[ny][nx] = 2 # 방문 완료
                    queue.append((ny, nx))
                    visited[ny][nx] = True

    count = 0
    for i in range(w):
        for j in range(h):
            if graph[j][i] == 1:
                bfs(j, i)
                count += 1

    print(count)