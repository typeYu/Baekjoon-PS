from itertools import combinations
N, L, R, X = map(int, input().split())
array = list(map(int, input().split()))

all_comb = []
for i in range(2, N + 1):
    comb = combinations(array, i)
    for c in comb:
        if L <= sum(c) <= R and (max(c) - min(c)) >= X:
            all_comb.append(c)

print(len(all_comb))