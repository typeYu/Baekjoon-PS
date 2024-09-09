N, S, M = map(int, input().split())
volume = list(map(int, input().split()))

d = [[0] * (M + 1) for _ in range(N)]
if 0 <= S + volume[0] <= M:
    d[0][S + volume[0]] = 1
if 0 <= S - volume[0] <= M:
    d[0][S - volume[0]] = 1

for i in range(1, N):
    for j in range(M + 1):
        if d[i - 1][j] == 1:
            if 0 <= j + volume[i] < M + 1:
                d[i][j + volume[i]] = 1
            if 0 <= j - volume[i] < M + 1:
                d[i][j - volume[i]] = 1

for k in range(M, -1, -1):
    if d[N - 1][k] == 1:
        print(k)
        exit()

print(-1)