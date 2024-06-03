from collections import deque
N, K = map(int, input().split())
visited = [0 for _ in range(100001)]

def bfs(N):
    queue = deque([N])
    visited[N] = 1
    while queue:
        q = queue.popleft()
        if q == K:
            return visited[q] - 1
        for dn in [q + 1, q - 1, 2 * q]:
            if 0 <= dn < 100001 and visited[dn] == 0:
                visited[dn] = visited[q] + 1
                queue.append(dn)

print(bfs(N))