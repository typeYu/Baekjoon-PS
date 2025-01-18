import sys
from collections import deque
N, M = map(int, sys.stdin.readline().strip().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(N)]
red_y, red_x = 0, 0
blue_y, blue_x = 0, 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 'R':
            red_y, red_x = i, j
        elif graph[i][j] == 'B':
            blue_y, blue_x = i, j

def move(y, x, dy, dx): # dy, dx 방향으로 최대한 이동
    cnt = 0
    while graph[y + dy][x + dx] != "#" and graph[y][x] != "O":
        y += dy
        x += dx
        cnt += 1
    return y, x, cnt

queue = deque([(red_y, red_x, blue_y, blue_x, 1)])
visited = set()
visited.add((red_y, red_x, blue_y, blue_x))

def bfs():
    while queue:
        red_y, red_x, blue_y, blue_x, count = queue.popleft()

        if count > 10:
            return 0

        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            red_ny, red_nx, red_cnt = move(red_y, red_x, dy, dx)
            blue_ny, blue_nx, blue_cnt = move(blue_y, blue_x, dy, dx)

            if graph[blue_ny][blue_nx] == 'O':
                continue

            if graph[red_ny][red_nx] == 'O':
                return 1

            # 둘의 위치가 겹칠 경우 더 많이 이동한 구슬을 한 칸 뒤로 ***
            if red_ny == blue_ny and red_nx == blue_nx:
                if red_cnt > blue_cnt:
                    red_ny -= dy
                    red_nx -= dx
                else:
                    blue_ny -= dy
                    blue_nx -= dx

            if (red_ny, red_nx, blue_ny, blue_nx) not in visited:
                visited.add((red_ny, red_nx, blue_ny, blue_nx))
                queue.append((red_ny, red_nx, blue_ny, blue_nx, count + 1))

    return 0

print(bfs())