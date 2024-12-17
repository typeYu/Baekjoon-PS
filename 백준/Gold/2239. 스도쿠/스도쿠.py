def row_check(y, num):
    for i in range(9):
        if graph[y][i] == num:
            return False
    return True

def column_check(x, num):
    for i in range(9):
        if graph[i][x] == num:
            return False
    return True

def three_check(y, x, num):
    y = (y // 3) * 3
    x = (x // 3) * 3
    for i in range(3):
        for j in range(3):
            if graph[y + i][x + j] == num:
                return False
    return True

def dfs(cnt):
    if cnt == len(zero):
        for i in range(9):
            print(''.join(map(str, graph[i])))
        exit()

    zy, zx = zero[cnt]
    for n in range(1, 10):
        if row_check(zy, n) and column_check(zx, n) and three_check(zy, zx, n):
            graph[zy][zx] = n
            dfs(cnt + 1)
            graph[zy][zx] = 0


graph = [list(map(int, input())) for _ in range(9)]
zero = []
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            zero.append((i, j))

dfs(0)