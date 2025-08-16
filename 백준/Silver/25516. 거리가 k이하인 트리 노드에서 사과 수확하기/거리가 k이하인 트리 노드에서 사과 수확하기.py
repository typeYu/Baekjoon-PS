import sys
from collections import deque
n, k = map(int, sys.stdin.readline().strip().split())
tree = [list() for _ in range(n)]
for _ in range(n - 1):
    parent, child = map(int, sys.stdin.readline().strip().split())
    tree[parent].append(child)
apple = list(map(int, sys.stdin.readline().strip().split()))


def bfs():
    cnt = 0
    queue = deque([(0, 0)])
    visited = [False] * n
    visited[0] = True

    while queue:
        q, dist = queue.popleft()
        if dist > k:
            continue
        else:
            if apple[q] > 0:
                cnt += 1
        for chd in tree[q]:
            if not visited[chd]:
                visited[chd] = True
                queue.append((chd, dist + 1))

    return cnt


print(bfs())