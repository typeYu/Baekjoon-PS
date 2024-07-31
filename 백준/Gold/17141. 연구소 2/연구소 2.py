from collections import deque
from itertools import combinations # 연구소1처럼 deepcopy해서 모든 좌표 구하면 시간초과 나서 바꿈
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
result = float('inf') # 초깃값을 무한대로 설정
virus_location = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            virus_location.append((i, j))

def bfs(location):
    time = 0
    max_second = 0
    visited = [[False] * N for _ in range(N)]
    second_mark = [[0] * N for _ in range(N)]
    queue = deque()

    for c_i, c_j in location:
        queue.append((c_i, c_j, time))
        visited[c_i][c_j] = True

    while queue:
        y, x, time = queue.popleft()
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and graph[ny][nx] != 1:
                queue.append((ny, nx, time + 1))
                visited[ny][nx] = True
                second_mark[ny][nx] = time + 1
                max_second = max(max_second, time + 1)

    for i in range(N):
        for j in range(N):
            if visited[i][j] == False and graph[i][j] != 1:
                return float('inf')
    return max_second


for c in combinations(virus_location, M):
    result = min(bfs(c), result)

if result == float('inf'):
    print(-1)
else:
    print(result)