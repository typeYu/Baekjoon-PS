from copy import deepcopy
N = int(input())
array = list(map(int, input().split()))
d = deepcopy(array)

for i in range(1, N):
    for j in range(i):
        if array[i] < array[j]:
            d[i] = max(d[i], d[j] + array[i])

print(max(d))
