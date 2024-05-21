from collections import deque
N = int(input())
r1, c1, r2, c2 = map(int, input().split())
graph = [[0] * N for _ in range(N)]

def bfs(x, y):
    graph[x][y] = 1
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        if x == r2 and y == c2:
            return graph[x][y]
        for dx, dy in [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0:
                queue.append((nx, ny))
                # 전의 그래프에서(graph[x][y]) +1 해줘야함 graph[nx][ny] + 1 하면 그래프에 1밖에 없음
                graph[nx][ny] = graph[x][y] + 1
a = bfs(r1, c1)
if a:
    print(a - 1)
else:
    print(-1)