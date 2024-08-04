import sys
for _ in range(int(input())):
    n = int(input())
    array1 = list(map(int, sys.stdin.readline().rstrip().split()))
    array2 = list(map(int, sys.stdin.readline().rstrip().split()))

    d = [[0, 0] for _ in range(n + 1)]
    d[1][0] = array1[0]
    d[1][1] = array2[0]

    for i in range(2, n + 1):
        d[i][0] = max(array1[i - 1] + d[i - 1][1], array1[i - 1] + d[i - 2][0], array1[i - 1] + d[i - 2][1])
        d[i][1] = max(array2[i - 1] + d[i - 1][0], array2[i - 1] + d[i - 2][1], array2[i - 1] + d[i - 2][0])

    print(max(d[n][0], d[n][1]))