from collections import deque
A, B = map(int, input().split())

visited = []
def bfs(A, B):
    count = 1
    queue = deque([(A, count)])
    visited.append(A)

    while queue:
        q, count = queue.popleft()
        if q == B:
            return count
        for nq in [q * 2, q * 10 + 1]:
            if nq not in visited and 0 <= nq <= B:
                queue.append((nq, count + 1))
                visited.append(nq)

    return -1

print(bfs(A, B))