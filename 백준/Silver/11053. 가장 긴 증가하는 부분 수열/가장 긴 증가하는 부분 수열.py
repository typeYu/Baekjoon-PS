N = int(input())
array = list(map(int, input().split()))
d = [1] * N
currentMax = array[0]
for i in range(1, len(array)):
    for j in range(i):
        if array[i] > array[j]:
            d[i] = max(d[i], d[j] + 1)
print(max(d))