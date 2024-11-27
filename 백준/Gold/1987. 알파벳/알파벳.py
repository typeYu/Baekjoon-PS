def dfs(i, j, cnt):
    global answer

    for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        ny, nx = i + dy, j + dx
        if 0 <= ny < R and 0 <= nx < C and visited[graph[ny][nx]] == 0:
            visited[graph[ny][nx]] = 1
            dfs(ny, nx, cnt + 1)
            visited[graph[ny][nx]] = 0

    answer = max(answer, cnt)
    return


R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]
visited = {chr(i): 0 for i in range(ord('A'), ord('Z') + 1)}
visited[graph[0][0]] = 1
answer = 0
dfs(0, 0, 1)

print(answer)