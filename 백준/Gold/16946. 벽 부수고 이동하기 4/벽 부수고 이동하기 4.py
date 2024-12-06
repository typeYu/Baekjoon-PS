from collections import deque
from copy import deepcopy

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
result_graph = deepcopy(graph)
color_dic = {}

# 0을 그룹으로 만들음
def zero_count(y, x, group_num):
    global graph

    count = 1
    queue = deque([(y, x)])
    graph[y][x] = group_num

    while queue:
        y, x = queue.popleft()
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] == 0:
                count += 1
                queue.append((ny, nx))
                graph[ny][nx] = group_num

    color_dic[group_num] = count

# 모든 0 좌표를 돌면서 그룹화
group_num = 2
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            graph[i][j] = -1
        elif graph[i][j] == 0:
            zero_count(i, j, group_num)
            group_num += 1


# 모든 1 좌표를 상하좌우 돌면서 답을 찾음
def up_down_left_right(y, x):
    all_group = []
    count = 1

    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] != -1:
            if graph[ny][nx] not in all_group:
                count += color_dic[graph[ny][nx]]
                all_group.append(graph[ny][nx])

    return count % 10


for i in range(N):
    for j in range(M):
        if result_graph[i][j] == 1:
            result_graph[i][j] = up_down_left_right(i, j)


for g in result_graph:
    print(''.join(map(str, g)))