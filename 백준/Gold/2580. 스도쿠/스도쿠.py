def is_true(y, x, num):
    for i in range(9):
        if graph[i][x] == num:
            return False
        if graph[y][i] == num:
            return False

    ty = (y // 3) * 3
    tx = (x // 3) * 3
    for i in range(3):
        for j in range(3):
            if graph[ty + i][tx + j] == num:
                return False

    return True

def dfs(depth):
    if depth == zeros_length:
        for g in graph:
            print(*g)
        exit()

    for each_num in range(1, 10):
        zeros_y = zeros[depth][0]
        zeros_x = zeros[depth][1]
        if is_true(zeros_y, zeros_x, each_num):
            graph[zeros_y][zeros_x] = each_num
            dfs(depth + 1)
            graph[zeros_y][zeros_x] = 0


graph = [list(map(int, input().split())) for _ in range(9)]
zeros = []
for y in range(9):
    for x in range(9):
        if graph[y][x] == 0:
            zeros.append((y, x))

zeros_length = len(zeros)
dfs(0)
