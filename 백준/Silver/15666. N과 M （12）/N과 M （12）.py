from itertools import combinations_with_replacement
N, M = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
a = combinations_with_replacement(array, M)
a = set(a)
for i in a:
    print(*i)