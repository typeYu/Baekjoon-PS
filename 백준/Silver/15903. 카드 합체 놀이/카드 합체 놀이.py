import sys
n, m = map(int, sys.stdin.readline().strip().split())
nums = list(map(int, sys.stdin.readline().strip().split()))
for i in range(m):
    nums.sort()
    a = nums[0]
    b = nums[1]
    nums[0] = a + b
    nums[1] = a + b
print(sum(nums))