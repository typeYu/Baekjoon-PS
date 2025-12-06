import sys
from collections import deque


def bfs():
    queue = deque([(y1, x1, 0)])
    visited = [[float('inf')] * M for _ in range(N)]
    visited[y1][x1] = 0

    while queue:
        y, x, cnt = queue.popleft()
        if y == y2 and x == x2:
            return cnt

        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            for k in range(1, K + 1):
                ny = y + dy * k
                nx = x + dx * k

                if not (0 <= ny < N and 0 <= nx < M):
                    break
                if graph[ny][nx] == '#':
                    break

                nxt_cnt = cnt + 1

                if visited[ny][nx] < nxt_cnt:  # 더 빠른 방문 존재 → break
                    break

                if visited[ny][nx] == nxt_cnt:  # 같은 시간 방문 존재 → 이 칸은 조사할 필요 없음
                    continue

                visited[ny][nx] = nxt_cnt
                queue.append((ny, nx, nxt_cnt))

    return -1


N, M, K = map(int, sys.stdin.readline().strip().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(N)]
y1, x1, y2, x2 = map(int, sys.stdin.readline().strip().split())
y1, x1, y2, x2 = y1 - 1, x1 - 1, y2 - 1, x2 - 1

print(bfs())
