import sys
from collections import deque
N, M = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
island1, island2 = map(int, sys.stdin.readline().strip().split())

start, end = 1, 1000000000

def binery_search(start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        if bfs(mid):
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    return result

def bfs(weight):
    queue = deque([island1])
    visited = [False] * (N + 1)
    visited[island1] = True

    while queue:
        island = queue.popleft()
        if island == island2:
            return True
        for next_node, w in graph[island]:
            if not visited[next_node] and w >= weight:
                visited[next_node] = True
                queue.append(next_node)

    return False

print(binery_search(start, end))