import sys
from collections import deque


def bfs():
    visited[1] = True
    queue = deque([1])
    record = [[-1, 1]] # 노드 1부터 시작하여 부모-자식 노드 기록

    while queue:
        q = queue.popleft()
        for nxt in graph[q]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)
                record.append([q, nxt])

    # 기록된 연결 노드들 중 맨 끝 노드부터 dp 시작
    for cur, nxt in reversed(record):

        # 현재 노드를 선택 하지 않는다면 반드시 다음 노드 선택
        dp[cur][0] += dp[nxt][1]
        # 현재 노드를 선택한다면, 다음 노드를 선택해도 되고 안해도 되고
        dp[cur][1] += min(dp[nxt][0], dp[nxt][1])


N = int(sys.stdin.readline())
graph = [list() for _ in range(N + 1)]
visited = [False] * (N + 1)
dp = [[0, 1] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

bfs()
print(min(dp[1]))