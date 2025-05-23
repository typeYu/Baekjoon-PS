import sys
from bisect import bisect_left
N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().strip().split()))
array.sort()

answer = float('inf')
for i in range(N):
    b = bisect_left(array, -array[i])

    for j in range(-1, 2):
        if b + j >= N or b + j < 0 or b + j == i:
            continue
        result = array[i] + array[b + j]
        if abs(result) < abs(answer):
            answer = result

print(answer)