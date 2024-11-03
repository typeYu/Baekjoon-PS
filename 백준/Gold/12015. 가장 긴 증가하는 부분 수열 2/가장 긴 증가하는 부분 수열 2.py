import sys
from bisect import bisect_left
N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().strip().split()))
lis = [array[0]]

for a in range(1, len(array)):
    if lis[-1] < array[a]:
        lis.append(array[a])
    else:
        idx = bisect_left(lis, array[a])
        lis[idx] = array[a]

print(len(lis))