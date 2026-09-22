def solution(x, y, n):
    if x == y:
        return 0
    
    dp = [float('inf')] * (y + 1)
    dp[x] = 0
    for i in range(x, y + 1):
        if i + n <= y:
            dp[i + n] = min(dp[i]+ 1, dp[i + n])
        
        if i * 2 <= y:
            dp[i * 2] = min(dp[i]+ 1, dp[i * 2])
        
        if i * 3 <= y:
            dp[i * 3] = min(dp[i]+ 1, dp[i * 3])
        
    if dp[y] == float('inf'):
        return -1
    else:
        return dp[y]
    