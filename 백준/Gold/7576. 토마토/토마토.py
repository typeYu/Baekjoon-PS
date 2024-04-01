from collections import deque
M, N = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


def bfs():
    # 날짜
    count = 0
    queue = deque()
    for i in range(M):
        for j in range(N):
            if graph[j][i] == 1:
                queue.append((j, i, count))
    while queue:
        y, x, count = queue.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] == 0:
                graph[ny][nx] = 1
                queue.append((ny, nx, count + 1))
    return count


result = bfs()
for i in graph:
    if 0 in i:
        print(-1)
        exit()
else:
    print(result)