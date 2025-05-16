import sys
M, N = map(int, sys.stdin.readline().strip().split())
array = list(map(int, sys.stdin.readline().strip().split()))

start, end = 1, max(array)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for a in array:
        cnt += a // mid

    if cnt < M:
        end = mid - 1
    else:
        start = mid + 1

print(end)