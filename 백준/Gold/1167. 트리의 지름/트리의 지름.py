import sys
import heapq
N = int(sys.stdin.readline())
graph = [list() for _ in range(N + 1)]
# 다익스트라: 그래프 저장할 때 [거리, 노드] 순으로 저장
for _ in range(N):
    array = list(map(int, sys.stdin.readline().strip().split()))
    for a in range(1, len(array[1:-1]), 2):
        graph[array[0]].append([array[a + 1], array[a]])

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
            cost = dist + dd
            if distance[dn] > cost:
                distance[dn] = cost
                heapq.heappush(queue, (cost, dn))

    max_length = 0
    max_index = 0
    for d in range(1, len(distance)):
        if max_length < distance[d]:
            max_length = distance[d]
            max_index = d

    return [max_index, max_length]

first_index, first_length = dijkstra(1)
second_index, second_length = dijkstra(first_index)
print(second_length)