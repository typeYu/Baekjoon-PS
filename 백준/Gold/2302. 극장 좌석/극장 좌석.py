N = int(input())
M = int(input())
fix = [False] * (N + 1)
for _ in range(M):
    fix[int(input())] = True

answer = 1
dp = [1] * (N + 1)
for i in range(2, N + 1):
    if fix[i]:
        answer *= dp[i - 1]
    elif fix[i - 1]:
        continue
    else:
        dp[i] = dp[i - 1] + dp[i - 2]
    if i == N:
        answer *= dp[-1]
print(answer)
