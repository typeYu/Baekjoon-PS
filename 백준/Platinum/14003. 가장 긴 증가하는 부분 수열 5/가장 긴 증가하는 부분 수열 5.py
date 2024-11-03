import sys
from bisect import bisect_left
N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().strip().split()))
lis = [array[0]]
dp = [0] * N

for a in range(1, len(array)):
    idx = bisect_left(lis, array[a])
    if lis[-1] < array[a]:
        lis.append(array[a])
    else:
        lis[idx] = array[a]
    dp[a] = idx

answer = len(lis)
print(answer)
answer_arr = []
for i in range(len(dp) - 1, -1, -1):
    if dp[i] == answer - 1:
        answer_arr.append(array[i])
        answer -= 1

answer_arr.reverse()
print(*answer_arr)
