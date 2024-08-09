from collections import deque
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]


def how_many_cheese():
    cheese_count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                cheese_count += 1

    return cheese_count


def bfs():
    count = 0
    visited = [[False] * M for _ in range(N)]
    queue = deque([(0, 0)])
    visited[0][0] = True
    is_air = [] # 공기에 닿은 치즈 위치 저장
    is_too_air = set() # 공기에 2면 이상 닿은 치즈 위치 저장


    while queue:
        y, x = queue.popleft()
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    if graph[ny][nx] == 0:
                        queue.append((ny, nx))
                    elif graph[ny][nx] == 1:
                        is_air.append((ny, nx))
                elif visited[ny][nx] and (ny, nx) in is_air:
                    is_too_air.add((ny, nx))

    for i, j in is_too_air:
        graph[i][j] = 0
        count += 1

    return count

cheese_count = how_many_cheese()
time = 0
while True:
    count = bfs()
    time += 1 # bfs 한 번 돌리면 time 증가
    cheese_count -= count
    if cheese_count == 0:
        print(time)
        break