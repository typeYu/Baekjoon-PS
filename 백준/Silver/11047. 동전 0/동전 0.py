import sys
N, K = map(int, sys.stdin.readline().strip().split())
array = []
count = 0
for _ in range(N):
    array.append(int(sys.stdin.readline().strip()))
array.reverse()
for i in array:
    if K >= i:
        count += K // i
        K = K % i
print(count)
