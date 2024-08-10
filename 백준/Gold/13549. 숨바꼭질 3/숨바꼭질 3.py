import heapq
N, K = map(int, input().split())
distance = [float('inf') for _ in range(100001)]

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start)) # 현재 노드에서부터 현재 노드 까지의 거리, 현재 노드
    distance[start] = 0 # 현재 노드부터 거리

    while queue:
        dist, now = heapq.heappop(queue) # 거리, 노드
        if distance[now] < dist:
            continue
        for dd, dn in [(dist, now * 2), (dist + 1, now + 1), (dist + 1, now - 1)]:
            if 0 <= dn < 100001 and distance[dn] > dd:
                heapq.heappush(queue, (dd, dn))
                distance[dn] = dd

    return distance[K]

print(dijkstra(N))