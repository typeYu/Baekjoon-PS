from itertools import permutations
N = int(input())
array = [i for i in range(1, N+1)]
a = permutations(array, N)
for i in a:
    print(*i)