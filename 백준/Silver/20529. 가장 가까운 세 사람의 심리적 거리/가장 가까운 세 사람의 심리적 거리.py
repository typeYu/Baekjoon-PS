import sys
from itertools import combinations

for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    arr = list(map(str, sys.stdin.readline().strip().split()))

    if N >= 33: # 비둘기집 원리
        print(0)
        continue

    answer = float('inf')
    comb = combinations(arr, 3)
    for a, b, c in comb:
        cnt = 0
        for i in range(4):
            if a[i] != b[i]:
                cnt += 1
            if b[i] != c[i]:
                cnt += 1
            if a[i] != c[i]:
                cnt += 1
        answer = min(answer, cnt)

    print(answer)