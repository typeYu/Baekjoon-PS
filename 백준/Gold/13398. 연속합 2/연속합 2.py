import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split()))
# dp = [[0, 0] for _ in range(n)] # dp를 [0, 0]으로 시작해서 dp[-1]이 되면 0이랑 비교하는데, 음수를 간과함
dp = [[-float('inf'), -float('inf')] for _ in range(n)]
for i in range(n):
    dp[i][0] = max(arr[i], dp[i - 1][0] + arr[i]) # 현재 숫자로 시작, 현재까지 더한 숫자
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + arr[i]) # 이 숫자를 고르지 않음, 전의 숫자를 고르지 않음

print(max(max(i) for i in dp))