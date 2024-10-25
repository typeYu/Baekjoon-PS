import sys
from collections import deque
N, M = map(int, sys.stdin.readline().strip().split())
graph = [list() for _ in range(N + 1)]
inDegree = [0] * (N + 1)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    inDegree[b] += 1

def topology_sort():
    result = []
    queue = deque()

    for i in range(1, N + 1): # 진입 차수가 0인 정점이라면
        if inDegree[i] == 0:
            queue.append(i)

    while queue:
        q = queue.popleft()
        result.append(q)
        for l in graph[q]:
            inDegree[l] -= 1
            if inDegree[l] == 0:
                queue.append(l)

    for r in result:
        print(r, end=' ')

topology_sort()