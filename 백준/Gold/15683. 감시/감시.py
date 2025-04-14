import sys
from copy import deepcopy
N, M = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
cctv = []
answer = float('inf')

for i in range(N):
    for j in range(M):
        if graph[i][j] != 0 and graph[i][j] != 6:
            cctv.append([graph[i][j], i, j]) # cctv 번호, y좌표, x좌표

cctv_cnt = len(cctv)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

d = [
    [],
    [[0], [1], [2], [3]], # 1번, d[number]
    [[0, 1], [2, 3]], # 2번
    [[0, 3], [3, 1], [1, 2], [2, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [0, 1, 3]],
    [[0, 1, 2, 3]] # 5번
]


def oversee(cp_graph, direct, y, x): # 감시를 진행하는 함수 (-1로 표시)
    another_cp_graph = deepcopy(cp_graph)
    for d in direct:
        ny, nx = y + dy[d], x + dx[d]
        while 0 <= ny < N and 0 <= nx < M and another_cp_graph[ny][nx] != 6:
            if another_cp_graph[ny][nx] == 0:
                another_cp_graph[ny][nx] = -1
            ny += dy[d]
            nx += dx[d]

    return another_cp_graph


def backtracking(idx, cp_graph): # 현재 진행되고 있는 cctv 목록의 인덱스, 현재 그래프
    # 만약 모든 cctv를 활성화했다면 사각지대 수를 세어 준다.
    if idx == cctv_cnt:
        global answer
        result = 0
        for i in range(N):
            for j in range(M):
                if cp_graph[i][j] == 0:
                    result += 1

        if answer > result:
            answer = result
        return

    number = cctv[idx][0]
    y = cctv[idx][1]
    x = cctv[idx][2]

    # cctv 번호에 맞춰 감시를 진행한다.
    for direct in d[number]:
        new_cp_graph = oversee(cp_graph, direct, y, x)
        backtracking(idx + 1, new_cp_graph)


backtracking(0, deepcopy(graph))
print(answer)
