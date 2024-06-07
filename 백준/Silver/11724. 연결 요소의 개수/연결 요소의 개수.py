from collections import deque
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(node):
    queue = deque([node])
    if not visited[node]:
        visited[node] = True
    while queue:
        q = queue.popleft()
        for i in graph[q]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

count = 0
for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        count += 1
print(count)