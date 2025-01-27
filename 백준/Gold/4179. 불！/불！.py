import sys
from collections import deque

def fire_time(fire):
    global graph
    queue = deque(fire)

    while queue:
        y, x, time = queue.popleft()
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < R and 0 <= nx < C and fire_time_map[ny][nx] == -1 and graph[ny][nx] != '#':
                queue.append((ny, nx, time + 1))
                fire_time_map[ny][nx] = time + 1

def jh_move(jh):
    queue = deque([jh])
    while queue:
        jh_y, jh_x, jh_t = queue.popleft()
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = jh_y + dy, jh_x + dx
            # 탈출 조건: 미로의 가장자리를 넘어갈 때
            if ny < 0 or ny >= R or nx < 0 or nx >= C:
                return jh_t + 1
            if 0 <= ny < R and 0 <= nx < C and graph[ny][nx] == '.' and visited[ny][nx] == 0:
                if fire_time_map[ny][nx] == -1 or fire_time_map[ny][nx] > jh_t + 1:
                    queue.append((ny, nx, jh_t + 1))
                    visited[ny][nx] = 1
    return "IMPOSSIBLE"

R, C = map(int, sys.stdin.readline().strip().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(R)]
fire = []
jh = (0, 0, 0)

# 불의 확산 시간을 기록할 2차원 배열 (-1로 초기화)
fire_time_map = [[-1] * C for _ in range(R)]
visited = [[0] * C for _ in range(R)]  # 지훈이의 방문 여부 기록

for i in range(R):
    for j in range(C):
        if graph[i][j] == 'F':
            fire.append((i, j, 0))
            fire_time_map[i][j] = 0  # 불의 시작점
        elif graph[i][j] == 'J':
            jh = (i, j, 0)

# 불을 먼저 퍼뜨리고 시간 기록
fire_time(fire)
print(jh_move(jh))