from copy import deepcopy
N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
dp = deepcopy(house)

for i in range(1, N): # 1, 2,.. (N - 1)
    for j in range(3): # 0, 1, 2
        j_1, j_2 = 0, 0
        if j == 0:
            j_1, j_2 = 1, 2
        elif j == 1:
            j_1, j_2 = 0, 2
        elif j == 2:
            j_1, j_2 = 0, 1
        dp[i][j] = min(dp[i][j] + dp[i - 1][j_1], dp[i][j] + dp[i - 1][j_2])

print(min(dp[N-1]))