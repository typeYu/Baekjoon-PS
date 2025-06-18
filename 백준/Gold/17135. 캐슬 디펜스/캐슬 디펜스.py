import sys
from itertools import combinations
from collections import deque
from copy import deepcopy
N, M, D = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
enemy = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            enemy.append((i, j))

archer_locations = list(combinations([i for i in range(M)], 3))
answer = 0


# 적과의 거리 계산해야 함
def select_enemy(y, x, grp):
    queue = deque([(y, x)])
    visited = [[False] * M for _ in range(y + 1)]
    visited[y][x] = True

    while queue:
        new_y, new_x = queue.popleft()
        if grp[new_y][new_x] == 1 and abs(y - new_y) + abs(x - new_x) <= D:
            return [new_y, new_x]
        for dy, dx in [(0, -1), (-1, 0), (0, 1)]:
            ny, nx = new_y + dy, new_x + dx
            if 0 <= ny < y and 0 <= nx < M and not visited[ny][nx]:
                queue.append((ny, nx))
                visited[ny][nx] = True

    return False


for k in range(len(archer_locations)):
    cnt = 0
    grp = deepcopy(graph)
    grp.append([0] * M) # 궁수가 위치한 가상의 행을 하나 더 만들어 줌
    for i in range(N, 0, -1): # 턴 당 궁수의 y좌표 (인덱스 N부터 시작)
        targets = set()
        for j in archer_locations[k]: # 세 궁수의 각 x좌표
            result = select_enemy(i, j, grp)
            if not result:
                continue
            targets.add(tuple(result))
            # enemy_y, enemy_x = result[0], result[1]
            # grp[enemy_y][enemy_x] = 0
            # cnt += 1
        for enemy_y, enemy_x in targets:
            if grp[enemy_y][enemy_x] == 1:
                grp[enemy_y][enemy_x] = 0
                cnt += 1
    answer = max(answer, cnt)

print(answer)