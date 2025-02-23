import sys
from collections import deque
from itertools import permutations
pan = [[list(map(int, sys.stdin.readline().strip().split())) for _ in range(5)] for _ in range(5)]
current = [[[0] * 5 for _ in range(5)] for _ in range(5)] # 현재 놓여 있는 판의 모양
dy = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]
answer = float('inf')

# 판 순서 선택 후 dfs 실행
def solve():
    for perm in permutations([0, 1, 2, 3, 4]):
        for i in range(5):
            current[perm[i]] = pan[i] # 판을 쌓을 수 있는 모든 조합 대로 현재 판 모양을 구성
        dfs(0)

# 판을 90도 회전하는 함수
def rotate(current):
    temp = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            temp[j][4 - i] = current[i][j]

    return temp

# 5 * 5 각 층을 돌리는 함수
def dfs(idx):
    if idx == 5: # 만약 판 다섯 개를 쌓았다면
        if current[4][4][4]: # 출구가 값이 0이 아니라면
            bfs(current) # bfs를 돌려서 최솟값을 알아냄
        return

    for i in range(4): # 각 층에서 총 판을 4번 돌림
        if current[0][0][0]: # 만약 입구가 0이 아니라면
            dfs(idx + 1) # 다음 층 돌리기
        current[idx] = rotate(current[idx]) # 현재 층 돌리기

# 입구부터 출구까지 최소 거리를 계산하는 함수
def bfs(arr):
    global answer
    visited = [[[0] * 5 for _ in range(5)] for _ in range(5)]
    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 0

    while queue:
        h, y, x, = queue.popleft()
        if h == 4 and y == 4 and x == 4:
            answer = min(answer, visited[4][4][4])
            if answer == 12:
                print(12)
                exit()
            return
        for k in range(6):
            nh, ny, nx = h + dh[k], y + dy[k], x + dx[k]
            if nh < 0 or nh >= 5 or ny < 0 or ny >= 5 or nx < 0 or nx >= 5:
                continue
            if arr[nh][ny][nx] == 0 or visited[nh][ny][nx] != 0:
                continue
            else:
                queue.append((nh, ny, nx))
                visited[nh][ny][nx] = visited[h][y][x] + 1


solve()
if answer == float('inf'):
    print(-1)
else:
    print(answer)