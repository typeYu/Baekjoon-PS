from itertools import permutations
N, M = map(int, input().split())
array = list(map(int, input().split()))
com = list(permutations(array, M))
com.sort()
for i in com:
    print(*i)