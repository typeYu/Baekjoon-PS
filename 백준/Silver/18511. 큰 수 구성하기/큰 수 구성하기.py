import sys
from itertools import product
from bisect import bisect_right
N, K = map(int, sys.stdin.readline().strip().split())
array = list(map(int, sys.stdin.readline().strip().split()))

all_nums = set()
for l in range(1, len(str(N)) + 1):
    for prod in product(array, repeat=l):
        make = int(''.join(map(str, prod)))
        all_nums.add(make)

all_nums = sorted(all_nums)

print(all_nums[bisect_right(all_nums, N) - 1])
