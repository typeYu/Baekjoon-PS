import sys
import heapq


def dijkstra(start):
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        dist, node = heapq.heappop(queue)
        if distance[node] < dist:
            continue
        for dd, dn in graph[node]:
            if dist + dd < distance[dn]:
                distance[dn] = dist + dd
                heapq.heappush(queue, (dist + dd, dn))

    return distance


for _ in range(int(sys.stdin.readline())):
    n, d, c = map(int, sys.stdin.readline().strip().split())
    graph = [list() for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().strip().split())
        graph[b].append([s, a]) # 거리, 노드

    result = dijkstra(c)
    total, time = 0, 0
    for r in result:
        if float("inf") > r >= 0:
            total += 1
            time = max(time, r)
    print(total, time)