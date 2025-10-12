import sys
N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().strip().split()))

if N == 1:
    print(0)
    exit()

dp = [[0, 0] for _ in range(N)] # i번째 수를 선택 안 함, 함

dp[0][0] = 0
dp[0][1] = array[0]

for i in range(1, N):
    dp[i][0] = dp[i - 1][1]
    dp[i][1] = min(dp[i - 1][1] + array[i], dp[i - 1][0] + array[i])

print(min(dp[-1][0], dp[-1][1]))