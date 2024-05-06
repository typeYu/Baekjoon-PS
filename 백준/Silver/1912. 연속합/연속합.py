N = int(input())
array = list(map(int, input().split()))
d = [0] * N
d[0] = array[0]
for i in range(1, len(array)):
    if array[i] + d[i-1] > array[i]:
        d[i] = array[i] + d[i-1]
    else:
        d[i] = array[i]
print(max(d))