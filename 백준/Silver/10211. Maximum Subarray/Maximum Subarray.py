for _ in range(int(input())):
    N = int(input())
    array = list(map(int, input().split()))
    dp = array[::]
    dp[0] = array[0]
    for i in range(1, N):
        dp[i] = max(dp[i], array[i] + dp[i - 1])
    print(max(dp))