from itertools import combinations
N, M = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
com = list(combinations(array, M))
for i in com:
    print(*i)