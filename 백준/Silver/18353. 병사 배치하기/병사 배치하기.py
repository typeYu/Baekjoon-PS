import sys
N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().strip().split()))
d = [1] * N

for i in range(1, N):
    for j in range(i):
        if array[i] < array[j]:
            d[i] = max(d[i], d[j] + 1)

print(N - max(d))