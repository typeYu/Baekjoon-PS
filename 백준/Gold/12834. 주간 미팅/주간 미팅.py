import sys
from collections import deque


def dijkstra(start, A, B):
    distance = [float('inf')] * (V + 1)
    queue = deque([(0, start)])
    distance[start] = 0

    while queue:
        dist, node = queue.popleft()
        if distance[node] < dist:
            continue
        for dd, dn in graph[node]:
            cost = dist + dd
            if cost < distance[dn]:
                distance[dn] = cost
                queue.append((cost, dn))

    result = 0
    for AB in [distance[A], distance[B]]:
        if AB == float('inf'):
            result += -1
        else:
            result += AB

    return result


N, V, E = map(int, sys.stdin.readline().strip().split())
A, B = map(int, sys.stdin.readline().strip().split())
Hi = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(V + 1)]

# 각 출발 노드에 [거리, 도착 노드] 입력 받아 저장
for _ in range(E):
    a, b, l = map(int, sys.stdin.readline().strip().split())
    graph[a].append([l, b])
    graph[b].append([l, a])

# 모든 팀원에 대해 다익스트라 수행
answer = 0
for h in Hi:
    answer += dijkstra(h, A, B)

print(answer)