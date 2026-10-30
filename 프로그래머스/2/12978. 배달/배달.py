import heapq
def solution(N, road, K):
    graph = [[float('inf')] * (N + 1) for _ in range(N + 1)]
    for a, b, dist in road:
        graph[a][b] = min(graph[a][b], dist)
        graph[b][a] = min(graph[b][a], dist)
    
    distance = [float('inf')] * (N + 1)
    distance[1] = 0
    queue = [(0, 1)]
    
    while queue:
        dist, node = heapq.heappop(queue)

        for i in range(1, N + 1):
            d = graph[node][i]
            new_dist = dist + d
            
            if distance[node] < dist:
                continue
                
            if new_dist < distance[i]:
                distance[i] = new_dist
                heapq.heappush(queue, (new_dist, i))
    
    answer = 0
    for i in range(1, N + 1):
        if distance[i] <= K:
            answer += 1
    
    return answer
    
