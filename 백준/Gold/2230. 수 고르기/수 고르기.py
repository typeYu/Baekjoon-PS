import sys
N, M = map(int, sys.stdin.readline().strip().split())
array = []
for _ in range(N):
    array.append(int(sys.stdin.readline()))

array.sort()
result, start, end = float('inf'), 0, 1
while end < N:
    if array[end] - array[start] >= M:
        result = min(result, array[end] - array[start])
        start += 1
        if start == end:
            end += 1
    else:
        end += 1

print(result)