from itertools import combinations
N, S = map(int, input().split())
nums = list(map(int, input().split()))
result = 0
for i in range(1, N+1):
    a = combinations(nums, i)
    for j in a:
        if sum(j) == S:
            result += 1
print(result)