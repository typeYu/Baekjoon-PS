import sys
N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().strip().split()))
array.insert(0, 0)
dp = [0] * (N + 1)

for i in range(1, N + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + array[j])

print(dp[N])
