# 풀다가 막힘: 3가지 오류 1. time != -1떄문에 동시 도착 막음,
# 2. time[ny][nx] == t이 아니라 t + 1, 3. 꽃이 되면 queue에서 꺼냈을 때 꽃이면 진행 안됨


import sys
from itertools import combinations
from collections import deque
from copy import deepcopy


def bfs(greens, reds):
    flower = 0
    flowers = set()

    graph_copy = deepcopy(graph)
    time = [[-1] * M for _ in range(N)]

    queue = deque()
    for i, j in greens:
        queue.append((i, j, 3, 0)) # green = 3
        graph_copy[i][j] = 3
        time[i][j] = 0

    for i, j in reds:
        queue.append((i, j, 4, 0)) # red = 4
        graph_copy[i][j] = 4
        time[i][j] = 0

    while queue:
        y, x, color, t = queue.popleft()
        if (y, x) in flowers:
            continue

        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = y + dy, x + dx

            if 0 > ny or ny >= N or 0 > nx or nx >= M:
                continue

            if graph[ny][nx] == 0:
                continue

            if graph_copy[ny][nx] == 1 or graph_copy[ny][nx] == 2:
                graph_copy[ny][nx] = color
                time[ny][nx] = t + 1
                queue.append((ny, nx, color, t + 1))

            # 꽃일 때
            elif color != graph_copy[ny][nx] and time[ny][nx] == t + 1 and (ny, nx) not in flowers:
                flowers.add((ny, nx))
                graph_copy[ny][nx] = 5 # 꽃 = 5
                flower += 1

    return flower


N, M, G, R = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
flower = 0

able = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            able.append((i, j))

for greens in combinations(able, G): # 초록 배양액을 뿌린 땅들
    green_set = set(greens)
    rest = [i for i in able if i not in green_set]

    for reds in combinations(rest, R): # 빨간 배양액을 뿌린 땅들
        result = bfs(greens, reds)

        flower = max(flower, result)

print(flower)