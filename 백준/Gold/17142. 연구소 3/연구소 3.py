# 비활성 바이러스: 활성화 된 바이러스와 마찬가지로 큐에 넣어 져서 퍼져야 하지만, 시간은 카운트 하지 않음
# 해결 방법: bfs 돌릴 땐 활성화가 시작된 바이러스도 graph에서의 0칸과 똑같이 queue에 넣음
# visited로 기록한 시간을 측정할 때, **원래 graph == 0인 부분만 체크해서** max_num에 넣어 준다.
# visited로 활성화 시킨 바이러스가 5초에 퍼졌다고 기록 했는데, 시간 측정 시 세주면 곤란
# 추가: 안 퍼뜨려도 모든 칸에 바이러스가 벽을 제외한 칸에 있다면, 0을 출력해 주고 종료해야 함

import sys
from collections import deque
from itertools import combinations


def bfs(virus_location):
    visited = [[-1] * N for _ in range(N)]
    queue = deque()
    for y, x in virus_location:
        visited[y][x] = 0
        queue.append((y, x))

    while queue:
        y, x = queue.popleft()
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == -1 and graph[ny][nx] != 1:
                queue.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1

    max_num = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1 and graph[i][j] != 1:
                return float('inf')
            if graph[i][j] == 0:
                max_num = max(max_num, visited[i][j])

    return max_num


N, M = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

virus = []
is_zero = False
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            virus.append((i, j))
        if graph[i][j] == 0:
            is_zero = True

if not is_zero:
    print(0)
    exit()

all_virus_comb = combinations(virus, M)

answer = float('inf')
for comb in all_virus_comb:
    answer = min(answer, bfs(comb))

if answer == float('inf'):
    print(-1)
else:
    print(answer)