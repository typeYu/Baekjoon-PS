n, m = map(int, input().split())
graph = [[0] * m for _ in range(n)]
queen = list(map(int, input().split()))
knight = list(map(int, input().split()))
pawn = list(map(int, input().split()))
for i in range(1, len(queen), 2):
    graph[queen[i] - 1][queen[i + 1] - 1] = 1 # queen = 1
for i in range(1, len(knight), 2):
    graph[knight[i] - 1][knight[i + 1] - 1] = 2 # knight = 2
for i in range(1, len(pawn), 2):
    graph[pawn[i] - 1][pawn[i + 1] - 1] = 3 # pawn = 3


def delete_queen(i, j):
    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
        ny, nx = i + dy, j + dx
        while True:
            if 0 <= ny < n and 0 <= nx < m and (graph[ny][nx] != 1  and graph[ny][nx] != 2 and graph[ny][nx] != 3):
                graph[ny][nx] = 4 # 갈 수 없음 = 4
                ny, nx = ny + dy, nx + dx
            else:
                break


def delete_kignt(i, j):
    for dy, dx in [(-1, -2), (-1, 2), (1, -2), (1, 2), (2, 1), (-2, -1), (2, -1), (-2, 1)]:
        ny, nx = i + dy, j + dx
        if 0 <= ny < n and 0 <= nx < m and (graph[ny][nx] != 1  and graph[ny][nx] != 2 and graph[ny][nx] != 3):
            graph[ny][nx] = 4


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            delete_queen(i, j)
        elif graph[i][j] == 2:
            delete_kignt(i, j)

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            result += 1

print(result)