import sys
from collections import deque


def bfs(i, j):
    global is_union
    
    queue = deque([(i, j)])
    visited[i][j] = True
    union = [(i, j)]
    sum_union = graph[i][j]

    while queue:
        y, x = queue.popleft()
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and L <= abs(graph[y][x] - graph[ny][nx]) <= R:
                visited[ny][nx] = True
                queue.append((ny, nx))
                union.append((ny, nx))
                sum_union += graph[ny][nx]

    l = len(union)
    if l >= 2:
        is_union = True

    sum_union //= l
    for y, x in union:
        graph[y][x] = sum_union
        

N, L, R = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
answer = 0

while True:
    visited = [[False] * N for _ in range(N)]
    is_union = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j)
    
    if not is_union:
        break
    else:
        answer += 1

print(answer)