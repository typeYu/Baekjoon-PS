def bingo_count():
    cnt = 0

    for i in range(5):
        if all(graph[i][j] == -1 for j in range(5)):
            cnt += 1

    for i in range(5):
        if all(graph[j][i] == -1 for j in range(5)):
            cnt += 1

    if all(graph[i][i] == -1 for i in range(5)):
        cnt += 1

    if all(graph[i][4 - i] == -1 for i in range(5)):
        cnt += 1

    return cnt


graph = [list(map(int, input().split())) for _ in range(5)]
dic = {}
num = 0

for i in range(5):
    for j in range(5):
        dic[graph[i][j]] = (i, j)

for i in range(5):
    call = list(map(int, input().split()))
    for j in range(5):
        num += 1
        y, x = dic[call[j]]
        graph[y][x] = -1

        if bingo_count() >= 3:
            print(num)
            exit()