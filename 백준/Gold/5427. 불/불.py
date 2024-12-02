import sys
from collections import deque


def fire_time(fire):
    global graph
    queue = deque(fire)

    while queue:
        y, x, time = queue.popleft()
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and graph[ny][nx] in ['.', '@']:
                queue.append((ny, nx, time + 1))
                graph[ny][nx] = time + 1


def sg_move(sg):
    queue = deque([sg])
    while queue:
        sg_y, sg_x, sg_t = queue.popleft()
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = sg_y + dy, sg_x + dx
            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                return sg_t + 1
            elif 0 <= ny < h and 0 <= nx < w and graph[ny][nx] not in ['@', '#', '*']:
                if graph[ny][nx] == '.':
                    queue.append((ny, nx, sg_t + 1))
                    graph[ny][nx] = '@'
                else: # 숫자일 때
                    if int(graph[ny][nx]) > sg_t + 1:
                        queue.append((ny, nx, sg_t + 1))
                        graph[ny][nx] = '@'

    return "IMPOSSIBLE"


N = int(sys.stdin.readline())
for _ in range(N):
    w, h = map(int, sys.stdin.readline().strip().split())
    graph = [list(sys.stdin.readline().strip()) for _ in range(h)]
    fire = []
    sg = (0, 0, 0)
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '*':
                fire.append((i, j, 0))
            elif graph[i][j] == '@':
                sg = (i, j, 0)

    fire_time(fire)
    print(sg_move(sg))

