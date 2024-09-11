import sys
N = int(sys.stdin.readline())
array = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().strip().split())
    array.append([a, b])

array.sort(key=lambda x: x[0])

d = [1] * N
for i in range(N):
    for j in range(i):
        if array[i][1] > array[j][1]:
            d[i] = max(d[i], d[j] + 1)

print(N - max(d))