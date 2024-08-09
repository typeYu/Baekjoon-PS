from collections import deque
R, C, T = map(int, input().split()) # 세로, 가로, T초 후 구하기
graph = [list(map(int, input().split())) for _ in range(R)]

air_purifier_location = []
for i in range(2, R - 2):
    if graph[i][0] == -1:
        air_purifier_location.append(i)
        air_purifier_location.append(i + 1)
        break

def dust_start():
    array = []
    for i in range(R):
        for j in range(C):
            if graph[i][j] != 0 and graph[i][j] != -1:
                array.append([i, j])
    return array

def dust_spread():
    dust = dust_start()
    queue = deque(dust)

    save = []  # 미세먼지가 퍼질 위치, 양 전부 저장
    while queue:
        y, x = queue.popleft()
        temp = [] # 상하좌우 탐색 후 여기에 저장
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < R and 0 <= nx < C and graph[ny][nx] != -1:
                temp.append((ny, nx))

        amount = graph[y][x] // 5
        for i, j in temp:
            save.append([i, j, amount])
        graph[y][x] -= amount * len(temp)

    for i, j, a in save:
        graph[i][j] += a


def air_move():
    for i in range(air_purifier_location[0] - 1, 0, -1): # 반시계 - 위에서 아래
        graph[i][0] = graph[i - 1][0]

    for i in range(C - 1): # 반시계 - 오른쪽에서 왼쪽
        graph[0][i] = graph[0][i + 1]

    for i in range(0, air_purifier_location[0]): # 반시계 - 아래에서 위
        graph[i][C - 1] = graph[i + 1][C - 1]

    for i in range(C - 1, 1, -1): # 반시계 - 왼쪽에서 오른쪽
        graph[air_purifier_location[0]][i] = graph[air_purifier_location[0]][i - 1]


    for i in range(air_purifier_location[1] + 1, R - 1): # 시계 - 아래에서 위
        graph[i][0] = graph[i + 1][0]

    for i in range(C - 1): # 시계 - 오 왼
        graph[R - 1][i] = graph[R - 1][i + 1]

    for i in range(R - 1, air_purifier_location[1], -1): #시계 위 아래
        graph[i][C - 1] = graph[i - 1][C - 1]

    for i in range(C - 1, 1, -1): # 시계 왼 오
        graph[air_purifier_location[1]][i] = graph[air_purifier_location[1]][i - 1]

    for i in range(air_purifier_location[0], air_purifier_location[0] + 2): # 공기청정기 옆 초기화
        graph[i][1] = 0


num = 0
while num < T:
    dust_spread()
    air_move()
    num += 1

result = 0
for i in range(R):
    for j in range(C):
        if graph[i][j] != -1:
            result += graph[i][j]

print(result)