import sys
from collections import deque


def bfs():
    queue = deque([(home_y, home_x)])
    visited = [False] * (n + 1)

    while queue:
        y, x = queue.popleft()
        if y == festival_y and x == festival_x:
            return "happy"
        for i in range(n + 1):
            if not visited[i]:
                dy, dx = cs[i][1], cs[i][0]
                if abs(y - dy) + abs(x - dx) <= 1000:
                    visited[i] = True
                    queue.append((dy, dx))

    return "sad"


for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    home_x, home_y = map(int, sys.stdin.readline().strip().split())
    cs = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
    festival_x, festival_y = map(int, sys.stdin.readline().strip().split())
    cs.append([festival_x, festival_y])

    print(bfs())