S1 = input()
S2 = input()
dp = [[''] * (len(S1) + 1) for _ in range(len(S2) + 1)]

for i in range(1, len(S2) + 1):
    for j in range(1, len(S1) + 1):
        if S2[i - 1] == S1[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + S2[i - 1]
        else:
            if len(dp[i - 1][j]) >= len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

print(len(dp[-1][-1]))
print(dp[-1][-1])