import sys
from collections import deque

def topology_sort():
    answer = []
    queue = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        q = queue.popleft()
        answer.append(q)
        for nxt in graph[q]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)

    if len(answer) == N:
        return answer
    else:
        return None

input = sys.stdin.readline
N, M = map(int, input().split())
indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    arr = list(map(int, input().split()))
    for i in range(1, len(arr) - 1):
        a, b = arr[i], arr[i + 1]
        graph[a].append(b)
        indegree[b] += 1

ans = topology_sort()
if ans is None:
    print(0)
else:
    print(*ans, sep="\n")
