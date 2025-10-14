import sys


def dfs(y, x, move, apple):
    global answer

    if apple == 3:
        answer = min(answer, move)
        return

    if move > answer:
        return

    for dy, dx in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < 5 and 0 <= nx < 5 and not visited[ny][nx] and graph[ny][nx] != -1:
            visited[ny][nx] = True
            dfs(ny, nx, move + 1, apple + 1 if graph[ny][nx] == 1 else apple)
            visited[ny][nx] = False


graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(5)]
start_y, start_x = map(int, sys.stdin.readline().strip().split())
answer = float('inf')
visited = [[False] * 5 for _ in range(5)]
visited[start_y][start_x] = True

dfs(start_y, start_x, 0, 0)

print(answer if answer != float('inf') else -1)