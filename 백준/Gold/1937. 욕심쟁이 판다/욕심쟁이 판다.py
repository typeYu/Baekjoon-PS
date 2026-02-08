# 사이클이 없는 그래프인지가 중요한가? 그냥 무시하고 풀기로 결심
# cnt가 필요 없다?? cnt는 가변인데 dp는 불변이어야 한다? 는 말을 듣고 cnt를 없애고 dp테이블에 기록하기로 함
# 틀림 - gpt
# dfs(y,x)는 반드시 int(그 칸에서 시작하는 최대 길이)를 리턴하게 만들어.
# 캐시가 있으면 return dp[y][x].
# 4방향 돌면서 갈 수 있으면 child = dfs(ny,nx) 먼저 받고 dp[y][x] = max(dp[y][x], child + 1).
# 갑자기 런타임 에러 (RecursionError) 10**6 했으나 메모리 초과
# python3로 제출

import sys
sys.setrecursionlimit(10**6)


def dfs(y, x):
    # 만약 기록되어 있는 것이 있다면, 반환
    if dp[y][x] > 1:
        return dp[y][x]

    # 기록 되어 있는 것이 없다면, 상하좌우 탐색 시작
    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ny, nx = y + dy, x + dx

        if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] > graph[y][x]:
            # 갈 수 있다면, 다음 칸으로 이동
            s = dfs(ny, nx)
            # 끝까지 간 후, 반환 값 + 1을 기록
            dp[y][x] = max(dp[y][x], s + 1)

    # 기록 된 숫자가 없는데 더 이상 상하좌우 탐색도 못하면, 그대로 반환
    return dp[y][x]


n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
dp = [[1] * n for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(n):
        dfs(i, j)

for i in range(n):
    for j in range(n):
        answer = max(answer, dp[i][j])
# print(dp)
print(answer)