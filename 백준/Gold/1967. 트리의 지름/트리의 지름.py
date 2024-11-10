# 루트 노드에서 제일 거리가 먼 노드를 구한 후, 다시 한번 그 노드에서 제일 먼 노드를 구하는 발상이 어려움
import sys
import heapq
N = int(sys.stdin.readline())
graph = [list() for _ in range(N)]
for _ in range(N - 1):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    graph[a - 1].append([c, b - 1])
    graph[b - 1].append([c, a - 1])

def dijkstra(start):
    distance = [float('inf') for _ in range(N)]
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, node = heapq.heappop(queue)
        if dist > distance[node]:
            continue
        for d, new_node in graph[node]:
            cost = dist + d
            if cost < distance[new_node]:
                distance[new_node] = cost
                heapq.heappush(queue, (cost, new_node))

    max_dist, answer_node = 0, 0
    for i in range(len(distance)):
        if distance[i] > max_dist:
            max_dist = distance[i]
            answer_node = i

    return answer_node, max_dist

first_node, max_dist = dijkstra(0)
second_node, answer = dijkstra(first_node)
print(answer)

