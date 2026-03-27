import sys
from bisect import bisect_left
n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
dp = [array[0]]

for i in range(1, n):
    idx = bisect_left(dp, array[i])
    if idx >= len(dp):
        dp.append(array[i])
    else:
        dp[idx] = array[i]

print(len(dp))