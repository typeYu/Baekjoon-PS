import heapq
number = 1
while True:
    N = int(input())
    if N == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(N)]
    distance = [[float('inf')] * N for _ in range(N)]

    def dijkstra():
        distance[0][0] = graph[0][0]
        queue = []
        heapq.heappush(queue, (graph[0][0], 0, 0))

        while queue:
            dist, y, x = heapq.heappop(queue)
            if distance[y][x] < dist:
                continue
            for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < N and dist + graph[ny][nx] < distance[ny][nx]:
                    distance[ny][nx] = dist + graph[ny][nx]
                    heapq.heappush(queue, (dist + graph[ny][nx], ny, nx))

        return distance[N - 1][N - 1]

    print(f"Problem {number}: {dijkstra()}")
    number += 1