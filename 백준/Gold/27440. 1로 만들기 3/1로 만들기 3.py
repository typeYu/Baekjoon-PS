import sys
from collections import deque

N = int(sys.stdin.readline())

def bfs(N):
    visited = {N: 0} # N이 최대 10**18이므로 visited 배열을 N개 만큼 선언하면 안됨
    queue = deque([N])

    while queue:
        q = queue.popleft()
        if q == 1:
            return visited[1]
        array = [q - 1]
        if q % 2 == 0:
            array.append(q // 2)
        if q % 3 == 0:
            array.append(q // 3)
        for i in array:
            if i >= 1 and i not in visited:
                visited[i] = visited[q] + 1
                queue.append(i)

print(bfs(N))