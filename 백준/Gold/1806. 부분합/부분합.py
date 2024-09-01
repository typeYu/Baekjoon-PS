import sys
N, S = map(int, input().split())
array = list(map(int, sys.stdin.readline().strip().split()))

start, end = 0, 0
result = float('inf')
sumAll = 0
for start in range(N):
    while sumAll < S and end < N:
        sumAll += array[end]
        end += 1
    if sumAll >= S:
        result = min(result, end - start)
    sumAll -= array[start]

if result == float('inf'):
    print(0)
else:
    print(result)