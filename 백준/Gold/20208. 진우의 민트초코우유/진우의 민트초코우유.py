N, M, H = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
home_y, home_x = 0, 0
mint = []
result = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            home_y, home_x = i, j
        elif graph[i][j] == 2:
            mint.append((i, j))

def backtracking(currenty, currentx, hp, count):
    global result

    for my, mx in mint:
        if graph[my][mx] == 2:
            dist = abs(my - currenty) + abs(mx - currentx)
            if dist <= hp:
                graph[my][mx] = 0
                backtracking(my, mx, hp - dist + H, count + 1)
                graph[my][mx] = 2

    home_dist = abs(currenty - home_y) + abs(currentx - home_x)
    if home_dist <= hp:
        result = max(result, count)

backtracking(home_y, home_x, M, 0)
print(result)