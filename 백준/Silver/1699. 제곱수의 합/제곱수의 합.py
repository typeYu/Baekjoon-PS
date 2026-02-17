N = int(input())
dp = [i + 1 for i in range(N)]
dp.insert(0, 0)

for num in range(int(N ** 0.5), 0, -1): # 제곱 가능한 수 역순으로
    num **= 2
    for i in range(num, N + 1):
        dp[i] = min(dp[i - num] + 1, dp[i])
print(dp[-1])
