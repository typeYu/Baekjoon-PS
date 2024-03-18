from itertools import combinations
N, M = map(int, input().split())
com = list(combinations(range(1, N+1), M))
for i in com:
    print(*i)