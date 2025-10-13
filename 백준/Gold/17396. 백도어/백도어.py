import sys
import heapq


def dijkstra(start):
    distance = [float('inf')] * N
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        dist, node = heapq.heappop(queue)
        if distance[node] < dist or enemy_sight[node] == 1:
            continue
        for d, n in array[node]:
            if dist + d < distance[n]:
                distance[n] = dist + d
                heapq.heappush(queue, (dist + d, n))

    return distance[-1]


N, M = map(int, sys.stdin.readline().strip().split())
enemy_sight = list(map(int, sys.stdin.readline().strip().split()))
enemy_sight[-1] = 0
array = [list() for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, sys.stdin.readline().strip().split())
    array[a].append([t, b])
    array[b].append([t, a])

answer = dijkstra(0)
print(answer if answer != float('inf') else -1)
