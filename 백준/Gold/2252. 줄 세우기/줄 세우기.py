import sys
from collections import deque
N, M = map(int, sys.stdin.readline().strip().split())
graph = [list() for _ in range(N + 1)]
inDegree = [0] * (N + 1)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    inDegree[b] += 1

def topology_sort(arr):
    result = arr
    queue = deque(arr)

    while queue:
        q = queue.popleft()
        for g in graph[q]:
            inDegree[g] -= 1
            if inDegree[g] == 0:
                queue.append(g)
                result.append(g)

    return result


zero_inDegree = []
for node in range(1, N + 1):
    if inDegree[node] == 0:
        zero_inDegree.append(node)

print(*topology_sort(zero_inDegree))

