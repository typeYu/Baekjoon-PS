import sys
from collections import deque


def bfs(start):
    queue = deque([start])
    visited = [False] * (N + 1)
    visited[start] = True
    cnt = 1

    while queue:
        q = queue.popleft()
        for i in graph[q]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                cnt += 1

    return [cnt, start]


N, M = map(int, sys.stdin.readline().strip().split())
graph = [list() for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().strip().split())
    graph[B].append(A)

answer_cnt = 0
answer = []
for computer in range(1, N + 1):
    c, s = bfs(computer)

    if c >= answer_cnt:
        if c == answer_cnt:
            answer.append(computer)
        else:
            answer_cnt = c
            answer = [computer]

answer.sort()
print(*answer)
