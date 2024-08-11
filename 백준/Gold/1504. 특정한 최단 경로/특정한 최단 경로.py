import sys
import heapq
N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

u, v = map(int, input().split())


def dijkstra(start, end):
    distance = [float('inf')] * (N + 1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for dd, dn in graph[now]:
            cost = dist + dd ######################
            if distance[dn] > cost:
                distance[dn] = cost
                heapq.heappush(queue, [cost, dn])
    return distance[end]

a = dijkstra(1, v) + dijkstra(v, u) + dijkstra(u, N)
b = dijkstra(1, u) + dijkstra(u, v) + dijkstra(v, N)
result = min(a, b)
if result == float('inf'):
    print(-1)
else:
    print(result)