N = int(input())
d = [[0] * 10 for _ in range(N)]

for i in range(1, 10):
    d[0][i] = 1

for i in range(1, N):
    for j in range(10):
        if j == 0:
            d[i][j] = d[i - 1][j + 1]
        elif j == 9:
            d[i][j] = d[i - 1][j - 1]
        else:
            d[i][j] = d[i - 1][j - 1] + d[i - 1][j + 1]

print(sum(d[N - 1]) % 1000000000)