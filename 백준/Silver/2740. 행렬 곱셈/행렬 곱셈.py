N, M = map(int, input().split())
array1, array2 = [], []
for _ in range(N):
    array1.append(list(map(int, input().split())))
M, K = map(int, input().split())
for _ in range(M):
    array2.append(list(map(int, input().split())))

result = [[0 for _ in range(K)] for _ in range(N)]
for i in range(N):
    for j in range(K):
        for k in range(M):
            result[i][j] += array1[i][k] * array2[k][j]

for i in result:
    for j in i:
        print(j, end=' ')
    print('')