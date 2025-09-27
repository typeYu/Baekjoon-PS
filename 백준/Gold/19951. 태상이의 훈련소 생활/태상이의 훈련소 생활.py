import sys
N, M = map(int, sys.stdin.readline().strip().split())
H = list(map(int, sys.stdin.readline().strip().split()))
H.insert(0, 0)
dp = [0] * (N + 1)
for _ in range(M):
    a, b, k = map(int, sys.stdin.readline().strip().split())
    dp[a] += k
    if b == N:
        continue
    dp[b + 1] -= k

for i in range(1, N + 1):
    dp[i] += dp[i - 1]
    H[i] += dp[i]

print(*H[1:])