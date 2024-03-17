from itertools import product
N, M = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
a = product(array, repeat=M)
a = set(a)
for i in a:
    print(*i)