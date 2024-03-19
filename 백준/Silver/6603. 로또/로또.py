from itertools import combinations
while True:
    nums = list(map(int, input().split()))
    if nums == [0]:
        break
    nums = nums[1:]
    a = combinations(nums, 6)
    for i in a:
        print(*i)
    print()