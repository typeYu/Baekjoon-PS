import heapq
N, M, X = map(int, input().split())
graph = [list() for _ in range(N + 1)]
for _ in range(M):
    start, end, T = map(int, input().split())
    graph[start].append([T, end])


def dijkstra(start, end):
    distance = [float('inf')] * (N + 1)
    distance[start] = 0
    queue = []
    heapq.heapify(queue)
    heapq.heappush(queue, (0, start))

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for dd, dn in graph[now]:
            if dist + dd < distance[dn]:
                distance[dn] = dist + dd
                heapq.heappush(queue, (dist + dd, dn))

    return distance[end]


result = 0
for i in range(1, N + 1):
    result = max(result, dijkstra(i, X) + dijkstra(X, i))

print(result)