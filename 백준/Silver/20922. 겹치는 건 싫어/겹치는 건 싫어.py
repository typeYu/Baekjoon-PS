import sys
N, K = map(int, sys.stdin.readline().strip().split())
array = list(map(int, sys.stdin.readline().strip().split()))
count = [0] * (max(array) + 1)
result = 0

start, end = 0, 0
while end < N:
    if count[array[end]] < K:
        count[array[end]] += 1
        end += 1
    else:
        count[array[start]] -= 1
        start += 1
    result = max(result, end - start)

print(result)
