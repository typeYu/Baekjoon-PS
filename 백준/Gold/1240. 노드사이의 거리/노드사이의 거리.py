import sys
import heapq


def dijkstra(start):
    distance = [float('inf')] * (N + 1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        dist, node = heapq.heappop(queue)
        if distance[node] < dist:
            continue
        for dd, dn in graph[node]:
            if distance[dn] > dist + dd:
                distance[dn] = dist + dd
                heapq.heappush(queue, (dist + dd, dn))

    return distance


N, M = map(int, sys.stdin.readline().strip().split())
graph = [list() for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, d = map(int, sys.stdin.readline().strip().split())
    graph[a].append([d, b])
    graph[b].append([d, a])
record = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    if record[a] != [] or record[b] != []:
        if record[a]:
            print(record[a][b])
        else:
            print(record[b][a])
    else:
        record[a] = dijkstra(a)
        print(record[a][b])