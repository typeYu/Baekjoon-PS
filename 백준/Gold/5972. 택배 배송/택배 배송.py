import sys
import heapq
N, M = map(int, sys.stdin.readline().strip().split())
graph = [list() for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

def dijkstra():
    distance = [float('inf')] * (N + 1)
    distance[1] = 0
    queue = []
    heapq.heappush(queue, [0, 1])

    while queue:
        dist, node = heapq.heappop(queue)
        if distance[node] < dist:
            continue
        for dd, dn in graph[node]:
            new_dist = dist + dd
            if distance[dn] > new_dist:
                distance[dn] = new_dist
                heapq.heappush(queue, [new_dist, dn])

    return distance[N]

print(dijkstra())