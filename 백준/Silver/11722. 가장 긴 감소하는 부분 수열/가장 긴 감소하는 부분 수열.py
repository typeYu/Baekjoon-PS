import sys
N = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().strip().split()))
d = [1] * N

for i in range(1, len(array)):
    for j in range(i):
        if array[i] < array[j]:
            d[i] = max(d[j] + 1, d[i])
print(max(d))