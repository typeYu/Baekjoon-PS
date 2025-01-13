import sys
from bisect import bisect_left
N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().strip().split()))
length = []

for i in range(N):
    if len(length) == 0:
        length.append(array[i])
    else:
        idx = bisect_left(length, array[i])
        if array[i] > length[-1]:
            length.append(array[i])
        else:
            if array[i] < length[idx]:
                length[idx] = array[i]
print(len(length))
