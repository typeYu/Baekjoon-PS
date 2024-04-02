import sys
N, K = map(int, input().split())
array = list(map(int, sys.stdin.readline().strip().split()))
prefixSum = []
sumK = 0
for i in range(K):
    sumK += array[i]
prefixSum.append(sumK)
zero = 0
for i in range(K, N):
    sumK += array[i]
    sumK -= array[zero]
    prefixSum.append(sumK)
    zero += 1
print(max(prefixSum))