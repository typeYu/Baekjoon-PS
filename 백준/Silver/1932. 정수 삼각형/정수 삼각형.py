from copy import deepcopy
N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]
d = deepcopy(triangle)

for i in range(1, N):
    for j in range(len(triangle[i])):
        if j > 0:
            d[i][j] = max(d[i][j], triangle[i][j] + d[i - 1][j - 1])
        if j < len(triangle[i]) - 1:
            d[i][j] = max(d[i][j], triangle[i][j] + d[i - 1][j])

print(max(d[N - 1]))