from collections import deque
N = int(input())
graph = [list(input()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]


def no(y, x, S): # 적록색약 no
    queue = deque([(y, x, S)])
    visited[y][x] = True

    while queue:
        y, x, S = queue.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and graph[ny][nx] == S:
                queue.append((ny, nx, S))
                visited[ny][nx] = True


count = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            no(i, j, graph[i][j])
            count += 1
print(count, end=' ')


def yes(y, x, S): # 적록색약 yes
    if S == 'G':
        another_color = 'R'
    elif S == 'R':
        another_color = 'G'
    else:
        another_color = 'B'

    queue = deque([(y, x, S)])
    visited[y][x] = True

    while queue:
        y, x, S = queue.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                if graph[ny][nx] == S or graph[ny][nx] == another_color:
                    queue.append((ny, nx, S))
                    visited[ny][nx] = True


visited = [[False] * N for _ in range(N)]
count = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            yes(i, j, graph[i][j])
            count += 1
print(count)