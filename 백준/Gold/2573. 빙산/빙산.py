import sys
from collections import deque
N, M = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
is_ice = set()
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        if graph[i][j] != 0:
            is_ice.add((i, j))


def melt():
    wirte_array = set()
    for i, j in is_ice:
        write = 0
        for k in range(4):
            if graph[i + dy[k]][j + dx[k]] == 0:
                write += 1

        wirte_array.add((i, j, graph[i][j] - write))

    for i, j, w in wirte_array:
        if w > 0:
            graph[i][j] = w
        else:
            is_ice.remove((i, j))
            graph[i][j] = 0


def bfs(y, x):
    global visited
    queue = deque([(y, x)])
    visited[y][x] = True

    while queue:
        y, x = queue.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and graph[ny][nx] != 0:
                queue.append((ny, nx))
                visited[ny][nx] = True


answer = 0
while len(is_ice) > 0:
    # 먼저 녹임
    melt()

    cnt = 0
    visited = [[False] * M for _ in range(N)]
    # 몇 덩어리로 쪼개졌는지 판별
    for y, x in is_ice:
        if not visited[y][x]:
            bfs(y, x)
            cnt += 1

     # 1년 지남
    answer += 1

    # 두 덩어리 이상으로 쪼개졌으면 answer 반환 후 종료
    if cnt >= 2:
        print(answer)
        break

else:
    print(0)