# 발상이 어렵다 (풀이 보고 풂)
import sys
N, K = map(int, sys.stdin.readline().strip().split())
array = list(map(int, sys.stdin.readline().strip().split()))
all_distance = []

for i in range(N - 1):
    all_distance.append(array[i + 1] - array[i])

all_distance.sort()

print(sum(all_distance[:N - K]))