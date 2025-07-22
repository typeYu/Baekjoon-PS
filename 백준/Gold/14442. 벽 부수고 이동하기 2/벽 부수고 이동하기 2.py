# visited를 3차원으로 구현해서 k도 표현해줘야 한다는 발상이 어려움
import sys
from collections import deque
N, M, K = map(int, sys.stdin.readline().strip().split())
array = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

def bfs():
    visited = [[[False] * (K + 1) for _ in range(M)] for _ in range(N)]
    queue = deque([(0, 0, K, 1)])
    visited[0][0][K] = True

    while queue:
        y, x, k, ans = queue.popleft()
        if y == N - 1 and x == M - 1:
            return ans

        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                if array[ny][nx] == 1 and k == 0:
                    continue
                # 벽이 있음
                elif array[ny][nx] == 1 and not visited[ny][nx][k - 1]:
                    visited[ny][nx][k - 1] = True
                    queue.append((ny, nx, k - 1, ans + 1))
                # 벽이 없음
                elif array[ny][nx] == 0 and not visited[ny][nx][k]:
                    visited[ny][nx][k] = True
                    queue.append((ny, nx, k, ans + 1))

    return -1

print(bfs())
