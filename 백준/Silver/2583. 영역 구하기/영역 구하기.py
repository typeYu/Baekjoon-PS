from collections import deque
M, N, K = map(int, input().split())
graph = [[0] * N for _ in range(M)]
for _ in range(K):
    y1, x1, y2, x2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            graph[x][y] = 1

def bfs(y, x):
    area = 1 # 시작 지점 1로 초기화
    queue = deque([(y, x)])
    graph[y][x] = 3 # 시작 지점 방문 표시
    while queue:
        y, x = queue.popleft()
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny = y + dy
            nx = x + dx
            if 0 <= nx < N and 0 <= ny < M and graph[ny][nx] == 0:
                queue.append((ny, nx)) # 탐색한 넓이 큐에 넣어줘야
                area += 1
                graph[ny][nx] = 3
    return area

result = []
count = 0
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            result.append(bfs(i, j))
            count += 1
result.sort()
print(count)
print(*result)