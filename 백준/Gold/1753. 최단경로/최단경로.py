import heapq
import sys
V, E = map(int, input().split())
K = int(input())
graph = [list() for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().strip().split())
    graph[u].append([w, v])

def dijkstra(start):
    distance = [float('INF')] * (V + 1)
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for nw, nv in graph[now]: # 거리, 다음 노드
            cost = dist + nw ############cost 계산 필수 !!!!!!!!!!!!!
            if distance[nv] > cost:
                heapq.heappush(queue, (cost, nv))
                distance[nv] = cost
    return distance

distances = dijkstra(K) # start, end로 함수를 계속 실행하지 말고 한번에 distance를 return해서 구함
# start는 K로 고정 돼 있으니까

for i in range(1, V + 1):
    if distances[i] == float('inf'):
        print("INF")
    else:
        print(distances[i])