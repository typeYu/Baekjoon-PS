import heapq
M, N = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
distance = [[float('inf')] * M for _ in range(N)]

def dijkstra():
    global distance
    distance[0][0] = 0
    queue = []
    heapq.heappush(queue, (0, 0, 0))

    while queue:
        dist, y, x = heapq.heappop(queue)
        if dist > distance[y][x]:
            continue
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                if graph[ny][nx] == 1:
                    cost = dist + graph[ny][nx]
                else:
                    cost = dist
                if cost < distance[ny][nx]:
                    distance[ny][nx] = cost
                    heapq.heappush(queue, (cost, ny, nx))
    return distance[N - 1][M - 1]

print(dijkstra())