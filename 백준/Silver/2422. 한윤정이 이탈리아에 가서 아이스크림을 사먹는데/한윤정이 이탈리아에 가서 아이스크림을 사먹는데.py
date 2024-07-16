import sys
from itertools import combinations
N, M = map(int, sys.stdin.readline().rstrip().split())
no_ab = set()

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    no_ab.add((a, b))

all_comb = combinations(range(1, N + 1), 3)

result = 0
for a, b, c in all_comb:
    if (a, b) not in no_ab and (b, c) not in no_ab and (a, c) not in no_ab \
            and (c, a) not in no_ab and (b, a) not in no_ab and (c, b) not in no_ab:
        result += 1

print(result)