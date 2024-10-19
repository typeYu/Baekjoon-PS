N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
cloud = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]

def move(di, si):
    global cloud
    d = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
    temp = []
    for y, x in cloud:
        ny, nx = (y + (d[di - 1][0] * si)) % N, (x + (d[di - 1][1] * si)) % N
        temp.append((ny, nx))
    cloud = temp

def rain():
    for y, x in cloud:
        graph[y][x] += 1

def magic():
    d = [(-1, -1), (1, -1), (-1, 1), (1, 1)]
    for y, x in cloud:
        count = 0
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and graph[ny][nx] > 0:
                count += 1
        graph[y][x] += count

def make_cloud():
    global cloud
    temp = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] >= 2 and (i, j) not in cloud:
                temp.append((i, j))
                graph[i][j] -= 2
    cloud = temp

for _ in range(M):
    di, si = map(int, input().split())
    move(di, si)
    rain()
    magic()
    make_cloud()

result = 0
for n in range(N):
    result += sum(graph[n])
print(result)
