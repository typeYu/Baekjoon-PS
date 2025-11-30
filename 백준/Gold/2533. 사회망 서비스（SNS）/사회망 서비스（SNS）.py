import sys
sys.setrecursionlimit(10**7)


def dfs(cur, parent):
    visited[cur] = True

    for nxt in graph[cur]:
        if nxt == parent:
            continue

        dfs(nxt, cur)

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

dfs(1, -1)
print(min(dp[1][0], dp[1][1]))