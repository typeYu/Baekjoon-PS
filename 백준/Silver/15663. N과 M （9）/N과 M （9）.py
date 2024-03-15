from itertools import permutations
N, M = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
a = permutations(array, M)
a = set(a)
for i in a:
    print(*i)