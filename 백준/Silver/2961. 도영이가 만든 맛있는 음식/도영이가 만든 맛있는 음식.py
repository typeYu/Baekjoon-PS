import sys
from itertools import combinations
N = int(input())
ingredient = []
for _ in range(N):
    s, b = map(int, sys.stdin.readline().rstrip().split())
    ingredient.append((s, b))

result = set()
for i in range(1, N + 1):
    comb = combinations(ingredient, i)

    for C in comb:
        sour_save, bitter_save = 1, 0
        for c in C:
            sour_save *= c[0]
            bitter_save += c[1]
        result.add(abs(sour_save - bitter_save))

print(min(result))
