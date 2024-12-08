import sys
N, M = map(int, sys.stdin.readline().strip().split())
array = list(map(int, sys.stdin.readline().strip().split()))
array.sort(reverse=True)
sumArr = sum(array)
minus = 0
minus_count = 0
for i in range(N):
    sumArr -= array[i]
    minus += array[i]
    minus_count += 1
    if sumArr <= minus:
        break

print(M // (minus_count + 1))