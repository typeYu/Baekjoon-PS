from collections import deque
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
baby = [2, 0, 0, 0] # 크기, y좌표, x좌표, 지금까지 먹은 물고기 수
fish = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            baby[1] = i
            baby[2] = j
            graph[i][j] = 0
        elif graph[i][j] > 0:
            fish.append([graph[i][j], i, j]) # 크기, y좌표, x좌표

def bfs(fish_y, fish_x): # 특정 물고기와의 거리 반환
    visited = [[False] * N for _ in range(N)]
    queue = deque([(baby[1], baby[2], 0)])
    visited[baby[1]][baby[2]] = True

    while queue:
        y, x, count = queue.popleft()
        if (y, x) == (fish_y, fish_x):
            return count
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and graph[ny][nx] <= baby[0]:
                queue.append((ny, nx, count + 1))
                visited[ny][nx] = True
    return None

result = 0
while True:
    calculate_fish = [] # [거리, y좌표, x좌표] append
    for size, fish_y, fish_x in fish:
        if size < baby[0]:
            fish_distance = bfs(fish_y, fish_x)
            if fish_distance is not None:
                calculate_fish.append((fish_distance, fish_y, fish_x))

    calculate_fish.sort(key=lambda x:(x[0], x[1], x[2]))
    if len(calculate_fish) == 0:
        print(result)
        break
    else:
        # 가장 가까운 물고기 정보
        new_distance, new_y, new_x = calculate_fish[0]
        new_size = graph[new_y][new_x]

        # 물고기 먹기
        result += new_distance
        fish.remove([new_size, new_y, new_x])
        baby[1], baby[2] = new_y, new_x
        baby[3] += 1

        # 아기 상어 크기 증가
        if baby[0] == baby[3]:
            baby[0] += 1
            baby[3] = 0