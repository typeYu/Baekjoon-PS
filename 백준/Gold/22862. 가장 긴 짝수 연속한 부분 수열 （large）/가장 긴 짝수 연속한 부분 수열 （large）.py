import sys
N, K = map(int, sys.stdin.readline().strip().split())
array = list(map(int, sys.stdin.readline().strip().split()))
start, end = 0, 0
result = 0
odd = 0
while end < N:

    if odd > K:
        if array[start] % 2 == 1:
            odd -= 1
        start += 1
        continue
    else:
        if array[end] % 2 == 1:
            odd += 1
        end += 1

    result = max(result, end - start - odd)

print(result)