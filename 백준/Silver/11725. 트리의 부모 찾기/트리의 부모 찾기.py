from collections import deque
import sys
N = int(input())
graph = [list() for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs():
    visited = [-1] * (N + 1)
    queue = deque([1])
    visited[1] = 0

    while queue:
        q = queue.popleft()
        for i in graph[q]:
            if visited[i] == -1:
                queue.append(i)
                visited[i] = q

    return visited

print(*bfs()[2:], sep='\n')
