from collections import deque
A, B, N, M = map(int, input().split())
visited = [0 for _ in range(100001)]

def bfs(N):
    visited[N] = 1
    queue = deque([N])
    while queue:
        dn = queue.popleft()
        if dn == M:
            return visited[M]
        for move in [dn - 1, dn + 1, dn + A, dn + B, dn -A, dn -B, dn * A, dn * B]:
            if 0 <= move < 100001 and not visited[move]:
                visited[move] = visited[dn] + 1
                queue.append(move)
print(bfs(N) - 1)