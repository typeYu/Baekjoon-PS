import sys
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(19)]
direct = [[(1, 0), (-1, 0)], [(0, -1), (0, 1)], [(1, -1), (-1, 1)], [(-1, -1), (1, 1)]]


def is_five(y, x):
    color = graph[y][x]

    # 4개의 방향에 대해서
    for d in direct:
        stones = [(y + 1, x + 1)]
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            # 만약 입력받은 돌과 색깔이 같다면 카운트를 더해감
            while True:
                if 0 <= ny < 19 and 0 <= nx < 19 and graph[ny][nx] == color:
                    stones.append((ny + 1, nx + 1))
                    ny += dy
                    nx += dx
                else:
                    break

        # 만약 카운트 결과가 정확히 5개라면
        if len(stones) == 5:
            stones.sort(key=lambda x: (x[1], x[0]))
            print(color)
            print(stones[0][0], stones[0][1])
            exit()


for i in range(19):
    for j in range(19):
        if graph[i][j] != 0:
            is_five(i, j)

print(0)