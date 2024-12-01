import heapq
N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
start, end = map(int, input().split())
prev_node = [-1] * (N + 1) # 경로 저장

def dijkstra(start):
    distance = [float('inf') for _ in range(N + 1)]
    distance[start] = 0
    queue = []
    heapq.heapify(queue)
    heapq.heappush(queue, (0, start))

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for dd, dn in graph[now]:
            if dist + dd < distance[dn]:
                distance[dn] = dist + dd
                prev_node[dn] = now
                heapq.heappush(queue, (dist + dd, dn))

    return distance[end]


print(dijkstra(start))
current = end
path = []
while current != -1:
    path.append(current)
    current = prev_node[current]

print(len(path))
path.reverse()
print(' '.join(map(str, path)))