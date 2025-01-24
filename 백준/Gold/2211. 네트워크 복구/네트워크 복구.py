import sys
import heapq

def dijkstra(start):
    previous = [0] * (N + 1) # 직전 노드 기록
    distance = [float('inf')] * (N + 1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        dist, node = heapq.heappop(queue)
        if dist > distance[node]:
            continue
        for dd, dn in graph[node]:
            new_dist = dist + dd
            if new_dist < distance[dn]:
                distance[dn] = new_dist
                heapq.heappush(queue, (new_dist, dn))
                previous[dn] = node # 직전 노드 기록

    return previous


N, M = map(int, sys.stdin.readline().strip().split())
graph = [list() for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    graph[a].append([c, b]) # 거리, 연결 되어 있는 노드
    graph[b].append([c, a])

# 모든 정점을 연결해야 하므로 연결해야하는 간선의 개수는 항상 N−1개이다. *****
print(N - 1)
previous = dijkstra(1)
for i in range(2, N + 1):
    print(i, previous[i])