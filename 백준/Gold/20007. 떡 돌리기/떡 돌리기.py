import sys
import heapq
N, M, X, Y = map(int, sys.stdin.readline().strip().split())
graph = [list() for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    graph[a].append([c, b]) # 거리, 이웃집
    graph[b].append([c, a]) # ********** 양방향 그래프임 빼먹음 주의 **********

def dijkstra(start):
    distance = [float('inf')] * N
    distance[start] = 0
    queue = [[0, start]]
    heapq.heapify(queue)

    while queue:
        dist, node = heapq.heappop(queue)
        if distance[node] < dist:
            continue
        for dd, dn in graph[node]:
            if distance[dn] > dist + dd:
                distance[dn] = dist + dd
                heapq.heappush(queue, [dist + dd, dn])

    return distance

result = 1
prefix_sum = 0
all_dist = dijkstra(Y)
all_dist.sort()
for i in all_dist:
    if i > X:
        print(-1)
        exit()
    else:
        if prefix_sum + 2 * i <= X:
            prefix_sum += 2 * i
        else:
            prefix_sum = 2 * i
            result += 1

print(result)