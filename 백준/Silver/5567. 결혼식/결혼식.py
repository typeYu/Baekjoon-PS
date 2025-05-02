import sys
from collections import deque
N = int(sys.stdin.readline())
graph = [list() for _ in range(N + 1)]
for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([(1, 0)]) # 학번, 차수
visited = [False] * (N + 1)
visited[1] = True
answer = 0
while queue:
    node, degree = queue.popleft()
    if degree > 2:
        continue
    elif 0 < degree <= 2:
        answer += 1
    for d in graph[node]:
        if not visited[d]:
            visited[d] = True
            queue.append((d, degree + 1))

print(answer)