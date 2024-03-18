from itertools import product
N, M = map(int, input().split())
com = product(range(1, N+1), repeat=M)
for i in com:
    print(*i)
