import sys
sys.setrecursionlimit(10**4)


def dfs(y, x):
    global answer

    if x == C - 2:
        answer += 1
        return True

    for dy, dx in [(-1, 1), (0, 1), (1, 1)]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < R and 0 <= nx < C and graph[ny][nx] != 'x':
            graph[ny][nx] = 'x'
            res = dfs(ny, nx)
            if res:
                return True

    return False


R, C = map(int, sys.stdin.readline().strip().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(R)]
answer = 0

for y in range(R):
    if graph[y][1] != 'x':
        graph[y][1] = 'x'
        dfs(y, 1)

print(answer)