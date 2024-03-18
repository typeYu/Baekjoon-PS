from itertools import permutations
N, M = map(int, input().split())
com = list(permutations(range(1, N+1), M))
for i in com:
    print(*i)