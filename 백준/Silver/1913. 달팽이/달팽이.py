N = int(input())
find = int(input())
graph = [[0] * N for _ in range(N)]
num = N ** 2
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
cur_d = 0
y, x = 0, 0
answer = 0

while num > 0:
    graph[y][x] = num

    if num == find:
        answer = (y, x)

    ny, nx = y + d[cur_d][0], x + d[cur_d][1]
    if 0 > ny or 0 > nx or N <= nx or N <= ny or graph[ny][nx] != 0:
        cur_d = (cur_d + 1) % 4
        ny, nx = y + d[cur_d][0], x + d[cur_d][1]

    y, x = ny, nx

    num -= 1

for g in graph:
    print(*g)

print(answer[0] + 1, answer[1] + 1)