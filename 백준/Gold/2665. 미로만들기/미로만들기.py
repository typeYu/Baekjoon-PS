import heapq
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
distance = [[float('inf')] * n for _ in range(n)]

def dijkstra():
    global distance
    queue = []
    heapq.heappush(queue, (0, 0, 0))
    distance[0][0] = 0

    while queue:
        dist, node_y, node_x = heapq.heappop(queue)
        # 새로 큐에서 꺼낸 거리가 기존 비용인 distance 배열의 비용보다 크다면 넘겨도 됨
        # visited 역할
        if dist > distance[node_y][node_x]:
            continue
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = node_y + dy, node_x + dx
            if 0 <= ny < n and 0 <= nx < n:
                # 조건에 맞게 비용을 계산한다. 1일 때 비용 그대로, 0일 때는 비용 1
                if graph[ny][nx] == 1:
                    cost = dist
                else:
                    cost = dist + 1

                # 새로 구한 비용이 그 전의 비용을 계산 한 배열인 distance의 ny, nx값보다 더 작을 때
                if cost < distance[ny][nx]:
                    distance[ny][nx] = cost
                    heapq.heappush(queue, (cost, ny, nx))

dijkstra()
print(distance[n - 1][n - 1])