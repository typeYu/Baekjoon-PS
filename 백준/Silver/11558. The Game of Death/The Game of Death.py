T = int(input())

while T > 0:
    N = int(input())
    graph = [list() for _ in range(N + 1)]

    def dfs(node):
        for d in graph[node]:
            if visited[d] == 0:
                visited[d] = visited[node] + 1
                dfs(d)

    for i in range(1, N + 1):
        call = int(input())
        graph[i].append(call)
    visited = [0] * (N + 1)
    dfs(1)
    if visited[N] == 0:
        print(0)
    else:
        print(visited[N])
    T -= 1