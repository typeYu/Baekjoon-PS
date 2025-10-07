import sys
N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().strip().split()))
dp = [[0] * 21 for _ in range(N - 1)]
dp[0][array[0]] = 1

for i in range(1, N - 1):
    for j in range(21):
        if dp[i - 1][j] > 0:
            if 21 > j - array[i] >= 0:
                dp[i][j - array[i]] += dp[i - 1][j]
            if 0 <= j + array[i] < 21:
                dp[i][j + array[i]] += dp[i - 1][j]

print(dp[-1][array[-1]])