S1 = input()
S2 = input()
dp = [[0] * (len(S1) + 1) for _ in range(len(S2) + 1)]

for i in range(1, len(S2) + 1):
    for j in range(1, len(S1) + 1):
        if S2[i - 1] == S1[j - 1]:
             dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(S2)][len(S1)])