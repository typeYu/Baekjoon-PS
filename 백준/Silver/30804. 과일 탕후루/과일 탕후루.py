import sys
from collections import deque
N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().strip().split()))

if N == 1:
    print(1)
    exit()

start, end = 0, 0
types = {array[0]: 1}
answer = 0

while start <= end < N:
    answer = max(answer, end - start + 1)
    if end == N - 1:
        break
    if array[end + 1] in types or len(types) < 2:
        if array[end + 1] in types:
            types[array[end + 1]] += 1
        else:
            types[array[end + 1]] = 1
        end += 1
    else:
        types[array[start]] -= 1
        if types[array[start]] == 0:
            types.pop(array[start])
        start += 1

print(answer)