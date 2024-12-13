def dfs(x, n):
    global result
    if x < 500:
        return
    if n == N:
        result += 1
        return
    
    x -= K
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(x + array[i], n + 1)
            visited[i] = False



N, K = map(int, input().split())
array = list(map(int, input().split()))
result = 0
visited = [False] * N

dfs(500, 0)
print(result)