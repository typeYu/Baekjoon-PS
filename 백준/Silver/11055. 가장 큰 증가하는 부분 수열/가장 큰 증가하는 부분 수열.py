N = int(input())
array = list(map(int, input().split()))
d = [i for i in array]
for i in range(len(array)):
    for j in range(i):
        if array[i] > array[j]:
            d[i] = max(d[i], array[i] + d[j])
print(max(d))