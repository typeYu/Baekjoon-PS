import sys
from collections import deque


def coloring(start):
    visited[start] = 1
    queue = deque([start])

    while queue:
        q = queue.popleft()
        for node in graph[q]:
            if not visited[node]:
                queue.append(node)
                if visited[q] == 1:
                    visited[node] = 2
                else:
                    visited[node] = 1
            # 만약 이미 칠해진 노드인데, 인접한 q와 색깔(1 혹은 2)이 같다면
            else:
                if visited[node] == visited[q]:
                    return "NO"

    return "YES"


for _ in range(int(sys.stdin.readline())):
    V, E = map(int, sys.stdin.readline().strip().split())
    graph = [list() for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for _ in range(E):
        u, v = map(int, sys.stdin.readline().strip().split())
        graph[u].append(v)
        graph[v].append(u)

    is_NO = False
    for i in range(1, V + 1):
        if not visited[i]:
            answer = coloring(i)
            if answer == "NO":
                is_NO = True
    if is_NO:
        print("NO")
    else:
        print("YES")