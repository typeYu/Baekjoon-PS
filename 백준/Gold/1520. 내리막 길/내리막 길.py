import sys
sys.setrecursionlimit(10 ** 9)


def dfs(y, x):
    # 만약 제일 오른쪽 아래 칸에 도달하면 1 반환(한 개의 경우를 찾은 것)
    if y == M - 1 and x == N - 1:
        return 1

    # 현재 좌표에 아직 한 번도 방문하지 않았을 때:
    if dp[y][x] == -1:
        # 방문 처리 = 0(아직 도달 하지는 않았지만 방문을 표시해준다)
        dp[y][x] = 0

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < M and 0 <= nx < N and graph[ny][nx] < graph[y][x]:
                dp[y][x] += dfs(ny, nx)

    # 현재 좌표에 방문한 적 있거나, 상하좌우 탐색이 끝났을 때 경로의 수 반환
    return dp[y][x]


M, N = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

print(dfs(0, 0))