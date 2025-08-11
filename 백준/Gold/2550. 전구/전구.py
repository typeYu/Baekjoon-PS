import sys
from bisect import bisect_left
N = int(sys.stdin.readline())
array1 = list(map(int, sys.stdin.readline().strip().split()))
array2 = list(map(int, sys.stdin.readline().strip().split()))

sort_arr = [[0, 0, i] for i in range(N + 1)] # 첫 번째 인덱스, 두 번째 인덱스, 진짜 숫자

for i in range(N):
    sort_arr[array1[i]][0] = i
    sort_arr[array2[i]][1] = i

sort_arr.sort(key=lambda x: (x[0], x[1]))

dp = []
real_num = []
for i in range(1, N + 1):
    idx = bisect_left(dp, sort_arr[i][1])
    if len(dp) == 0:
        dp.append(sort_arr[i][1])
    else:
        if dp[-1] < sort_arr[i][1]:
            dp.append(sort_arr[i][1])
        else:
            dp[idx] = sort_arr[i][1]

    real_num.append(idx)

answer = len(dp)
print(answer)

answer -= 1
answer_array = []
for i in range(N - 1, -1, -1):
    if real_num[i] == answer:
        answer_array.append(sort_arr[i + 1][2])
        answer -= 1

answer_array.sort()
print(*answer_array)