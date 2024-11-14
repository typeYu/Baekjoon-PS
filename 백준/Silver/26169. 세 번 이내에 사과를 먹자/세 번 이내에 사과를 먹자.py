graph = [list(map(int, input().split())) for _ in range(5)]
y, x = map(int, input().split())
graph[y][x] = -1

def dfs(i, j, cnt, apple):
    global graph

    if apple == 2:
        print(1)
        exit()
    elif cnt == 3:
        return

    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ny, nx = i + dy, j + dx
        if 0 <= ny < 5 and 0 <= nx < 5 and graph[ny][nx] != -1:
            temp = graph[ny][nx] # 주의) 원래 상태가 0, 1 두개이기 때문에 복구하려면 저장해야
            if graph[ny][nx] == 1:
                graph[ny][nx] = -1
                dfs(ny, nx, cnt + 1, apple + 1)
            else:
                graph[ny][nx] = -1
                dfs(ny, nx, cnt + 1, apple)
            graph[ny][nx] = temp

dfs(y, x, 0, 0)
print(0)