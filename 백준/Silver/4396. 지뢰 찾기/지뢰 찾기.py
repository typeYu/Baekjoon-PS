n = int(input())
bomb, find = [list(input()) for _ in range(n)], [list(input()) for _ in range(n)]
eight = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1)]
result = [['.'] * n for _ in range(n)]
is_Bomb = False

for i in range(n):
    for j in range(n):
        if find[i][j] == 'x':
            if bomb[i][j] == '*':
                result[i][j] = '*'
                is_Bomb = True
            else:
                around = 0
                for dy, dx in eight:
                    if 0 <= i+dy < n and 0 <= j+dx < n:
                        if bomb[i + dy][j + dx] == '*':
                            around += 1
                result[i][j] = str(around)

if is_Bomb:
    for i in range(n):
        for j in range(n):
            if bomb[i][j] == '*':
                result[i][j] = '*'

for i in result:
    for j in i:
        print(j, end="")
    print()