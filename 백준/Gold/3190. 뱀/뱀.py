import sys
from collections import deque
N = int(sys.stdin.readline())
graph = [[0] * N for _ in range(N)]
for _ in range(int(sys.stdin.readline())):
    i, j = map(int, sys.stdin.readline().strip().split())
    graph[i - 1][j - 1] = 4 # 사과
current = 0
direct = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 오른쪽, 아래, 왼쪽, 위
convert = deque() # 시간, 바꿀 방향 순으로 저장
for _ in range(int(sys.stdin.readline())):
    X, C = sys.stdin.readline().strip().split()
    convert.append((int(X), C))

movement = deque([(0, 0)])
graph[0][0] = 1 # 뱀
time = 0
while True:
    dy, dx = direct[current] # 이동
    head_y, head_x = movement[-1]
    head_ny = head_y + dy
    head_nx = head_x + dx
    time += 1

    if head_ny < 0 or head_ny >= N or head_nx < 0 or head_nx >= N or graph[head_ny][head_nx] == 1:
        break
    elif graph[head_ny][head_nx] == 0:
        tail_y, tail_x = movement.popleft()
        graph[tail_y][tail_x] = 0
    graph[head_ny][head_nx] = 1
    movement.append((head_ny, head_nx))

    if convert: # 매 시간마다 방향 바꿔야 하는지 체크
        ct, cd = convert.popleft()
        if ct == time:
            if cd == "L":
                current = (current + 3) % 4
            else:
                current = (current + 1) % 4
        else:
            convert.appendleft((ct, cd))

print(time)