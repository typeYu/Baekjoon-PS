import sys
sys.setrecursionlimit(10**7)

def dfs(cur, parent):
    visited[cur] = True
    dp[cur] = 1
    for node in graph[cur]:
        if node != parent:
            dfs(node, cur)
            dp[cur] += dp[node]

N, R, Q = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
dp = [0] * (N + 1)

for _ in range(N - 1):
    U, V = map(int, sys.stdin.readline().strip().split())
    graph[U].append(V)
    graph[V].append(U)

dfs(R, -1)

for _ in range(Q):
    U = int(sys.stdin.readline())
    print(dp[U])
