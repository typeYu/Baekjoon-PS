import sys
N, M = map(int, input().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))
total = 0
end = 0
count = 0
for start in range(N):
    while total < M and end < N:
        total += array[end]
        end += 1
    if total == M:
        count += 1
    total -= array[start]
print(count)