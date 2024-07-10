from collections import deque
N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split()) # S초 후, X, Y

save = []
for y in range(N):
    for x in range(N):
        if graph[y][x] != 0:
            save.append([y, x, graph[y][x], 0]) # 좌표, 바이러스 이름, 시간

save.sort(key=lambda x: x[2])

visited = [[False] * N for _ in range(N)]
def bfs(save):
    queue = deque(save)

    while queue:
        y, x, virus, second = queue.popleft()
        if second >= S: # 현재 초가 우리가 구해야 하는 S 이상이라면
            continue # 더 이상 진행하지 않음
        visited[y][x] = True
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and graph[ny][nx] == 0:
                queue.append([ny, nx, virus, second + 1])
                graph[ny][nx] = virus
                visited[ny][nx] = True
    return graph[X - 1][Y - 1]

print(bfs(save))