import sys

N, M = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

dy = [1, 1, 1]
dx = [-1, 0, 1]

min_fuel = float('inf')

def dfs(y, x, prev_dir, fuel):
    global min_fuel
    if y == N - 1:
        min_fuel = min(min_fuel, fuel)
        return
    for dir in range(3):
        if dir == prev_dir:
            continue
        ny = y + dy[dir]
        nx = x + dx[dir]
        if 0 <= ny < N and 0 <= nx < M:
            dfs(ny, nx, dir, fuel + board[ny][nx])

for x in range(M):
    dfs(0, x, -1, board[0][x])

print(min_fuel)
