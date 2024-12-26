import sys
from collections import deque
N, M = map(int, sys.stdin.readline().strip().split())
graph = [list() for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)
S, E = map(int, sys.stdin.readline().strip().split())

# 사전 순을 위해 정렬하기
for g in graph:
    g.sort()

# S > E bfs
answer1 = []
visited = [False] * (N + 1)
visited[S] = True
queue = deque([(S, [S])])
while queue:
    q, route = queue.popleft()
    if q == E:
        answer1 = route
        break
    for d in graph[q]:
        if not visited[d]:
            visited[d] = True
            queue.append((d, route + [d]))

# E > S bfs
answer2 = []
visited = [False] * (N + 1)
for v in answer1[1:]:
    visited[v] = True
queue = deque([(E, [E])])
while queue:
    q, route = queue.popleft()
    if q == S:
        answer2 = route
        break
    for d in graph[q]:
        if not visited[d]:
            visited[d] = True
            queue.append((d, route + [d]))

print(len(answer1) + len(answer2) - 2)