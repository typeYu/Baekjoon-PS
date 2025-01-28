# 처음에 푼 방식대로 다익스트라를 한 번만 돌리면, g~h를 거치는 경로가 최단 거리여도 놓칠 수 있음
# 다익스트라를 3번 돌려서 g~h를 강제로 거치게 한 후 최단 거리인지 확인한다.
import sys
import heapq


def dijkstra(start):
    # 만약 목적지에 도달할 수 없으면 공백을 출력해야 하는데, distance를 float('inf')로 설정하게 되면
    # INF + INF = INF가 되어 정답 처리를 하게 됨: float('inf')를 쓰면 X
    distance = [int(1e9)] * (n + 1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        dist, node = heapq.heappop(queue)
        if dist > distance[node]:
            continue
        for dd, dn in graph[node]:
            if dist + dd < distance[dn]:
                distance[dn] = dist + dd
                heapq.heappush(queue, (dist + dd, dn))

    return distance


for _ in range(int(sys.stdin.readline())):
    n, m, t = map(int, sys.stdin.readline().strip().split()) # 교차로, 도로, 목적지 개수
    graph = [list() for _ in range(n + 1)]
    s, g, h = map(int, sys.stdin.readline().strip().split()) # 시작, 지나가는 길 g, h
    for _ in range(m):
        a, b, d = map(int, sys.stdin.readline().strip().split())
        graph[a].append([d, b])
        graph[b].append([d, a])
    destination = [] # 목적지 후보
    for _ in range(t):
        destination.append(int(sys.stdin.readline()))

    start = dijkstra(s) # 시작 노드로부터 모든 노드까지의 최단 거리 기록
    g_distance = dijkstra(g) # g에서 모든 노드까지의 최단 거리
    h_distance = dijkstra(h)

    answer = []
    # 시작 노드 + g, h + 목적지 후보 노드 길이 구하기
    for i in destination:
        # 시작 노드에서 목적지 노드로 가는 최단 경로의 길이와 g~h를 거쳐서 가는 경로 길이와 같으면
        if start[i] == start[g] + g_distance[h] + h_distance[i] or start[i] == start[h] + h_distance[g] + g_distance[i]:
            answer.append(i)

    answer.sort()
    print(*answer)