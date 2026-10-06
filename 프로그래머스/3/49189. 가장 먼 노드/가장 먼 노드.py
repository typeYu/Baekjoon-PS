import heapq
def solution(n, edge):
    graph = [list() for _ in range(n + 1)]
    for e1, e2 in edge:
        graph[e1].append(e2)
        graph[e2].append(e1)
    
    distance = [float('inf')] * (n + 1)
    distance[0], distance[1] = 0, 0
    queue = []
    heapq.heappush(queue, [0, 1])
    while queue:
        dist, node = heapq.heappop(queue)
        if distance[node] < dist:
            continue
        for dn in graph[node]:
            dd = dist + 1
            if distance[dn] > dd:
                distance[dn] = dd
                heapq.heappush(queue, [dd, dn])
    
    
    return distance.count(max(distance))
    