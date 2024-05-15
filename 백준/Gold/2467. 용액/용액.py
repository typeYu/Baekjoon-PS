import sys
from bisect import bisect_left
N = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().rstrip().split()))
result = [1000000000, 999999999]
for i in range(len(array)):
    a = bisect_left(array, 0 - array[i])
    for j in range(-1, 2):
        if 0 < a + j < N and a + j != i:
            a = a + j
            if abs(array[a] + array[i]) < abs(sum(result)):
                result[0], result[1] = array[a], array[i]
result.sort()
print(*result)