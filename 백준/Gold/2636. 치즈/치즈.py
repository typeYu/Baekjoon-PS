from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
save = []

def bfs():
    queue = deque([(0, 0)])
    visited[0][0] = True
    count = 0

    while queue:
        y, x = queue.popleft()
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                visited[ny][nx] = True
                if graph[ny][nx] == 1:
                    count += 1
                    graph[ny][nx] = 0
                else:
                    queue.append((ny, nx))
    save.append(count)
    return count

time = 0
while True:
    visited = [[False] * M for _ in range(N)]
    result = bfs()

    if result == 0:
        print(time)
        print(save[-2] if len(save) > 1 else 0)
        break
    time += 1
