def validation(y, x, dir):
    ny, nx = y + d[dir][0], x + d[dir][1]
    while 0 <= ny < 8 and 0 <= nx < 8:
        if graph[ny][nx] == '*':
            return False

        ny += d[dir][0]
        nx += d[dir][1]

    return True

graph = [list(input()) for _ in range(8)]

queens = []
for i in range(8):
    for j in range(8):
        if graph[i][j] == '*':
            queens.append((i, j))

if len(queens) != 8:
    print("invalid")
    exit()

d = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

for qy, qx in queens:
    for dd in range(8):
        if not validation(qy, qx, dd):
            print("invalid")
            exit()

print("valid")