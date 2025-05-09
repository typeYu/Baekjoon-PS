import sys
from itertools import permutations
N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().strip().split()))
per = permutations(array, N)

answer = 0
for p in per:
    total = 0
    for idx in range(N - 1):
        total += abs(p[idx] - p[idx + 1])

    answer = max(answer, total)

print(answer)