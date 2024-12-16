import sys
from bisect import bisect_left
N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().strip().split()))
array.sort()
result = [float('inf'), float('inf'), float('inf')]

for a in range(1, N):
    for b in range(a):
        tempC = bisect_left(array, -(array[a] + array[b]))
        for i in range(-1, 2, 1):
            c = tempC + i
            if 0 <= c < N and c != a and c != b and abs(sum(result)) > abs(array[a] + array[b] + array[c]):
                result = [array[a], array[b], array[c]]

result.sort()
print(*result)