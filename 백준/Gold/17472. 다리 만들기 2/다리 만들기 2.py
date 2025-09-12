import sys
from collections import deque

def find_parnets(a):
    if a != parent[a]:
        parent[a] = find_parnets(parent[a])
    return parent[a]

def union_parents(a, b):
    a_p = find_parnets(a)
    b_p = find_parnets(b)
    if a_p != b_p:
        if a_p < b_p:
            parent[b_p] = find_parnets(a_p)
        else:
            parent[a_p] = find_parnets(b_p)

def islands_name(i, j):
    global island_name
    graph[i][j] = island_name
    queue = deque([(i, j)])
    visited = [[False] * M for _ in range(N)]
    visited[i][j] = True
    locations = []
    locations.append([i, j])

    while queue:
        y, x = queue.popleft()
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and graph[ny][nx] == 1:
                graph[ny][nx] = island_name
                visited[ny][nx] = True
                queue.append((ny, nx))
                locations.append([ny, nx])

    return locations

# 다리를 bfs가 아니라 직선으로 만들어야 함
def distance_between_islands(locations1, another):
    best = float('inf')

    for y, x in locations1:
        cur = graph[y][x]

        # 네 방향으로 "직선"으로만 쭉 뻗어가며 탐색
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny = y + dy
            nx = x + dx
            length = 0

            while 0 <= ny < N and 0 <= nx < M:
                cell = graph[ny][nx]

                # 바다이면 계속 직진
                if cell == 0:
                    length += 1
                    ny += dy
                    nx += dx
                    continue

                # 자기 섬을 다시 만나면 이 방향은 불가
                if cell == cur:
                    break

                # 목표 섬을 만났고, 길이가 2 이상이면 후보 갱신
                if cell == another:
                    if 2 <= length < best:
                        best = length
                    break

                # 다른 섬을 만나면 막힘
                break

    return best


N, M = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

island_name = 2
all_locations = dict()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            all_locations[island_name] = islands_name(i, j)
            island_name += 1

parent = {i: i for i in range(2, island_name)}
distance = []

for i in range(2, island_name):
    for j in range(i, island_name):
        if i == j:
            continue
        dist = distance_between_islands(all_locations[i], j)
        distance.append([dist, i, j])

distance.sort(key=lambda x: x[0])
answer = 0

for d, island1, island2 in distance:
    p_1 = find_parnets(island1)
    p_2 = find_parnets(island2)
    if p_1 != p_2:
        union_parents(island1, island2)
        answer += d

if answer == float('inf'):
    print(-1)
else:
    print(answer)
