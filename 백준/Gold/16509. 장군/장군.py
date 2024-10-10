from collections import deque
sang = list(map(int, input().split()))
king = list(map(int, input().split()))

one = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우 한 칸 가는 것
two = [[(-1, -1), (-1, 1)], [(1, -1), (1, 1)], [(-1, -1), (1, -1)], [(-1, 1), (1, 1)]]

def is_valid(y, x):
    return 0 <= y < 10 and 0 <= x < 9

def is_king(y, x): # 왕이 있는지
    return y == king[0] and x == king[1]

def bfs(i, j):
    visited = [[False] * 9 for _ in range(10)]
    visited[i][j] = True
    queue = deque([(i, j, 0)])

    while queue:
        y, x, count = queue.popleft()

        if y == king[0] and x == king[1]:
            return count

        for i in range(4): # 상하좌우
            ny, nx = y + one[i][0], x + one[i][1] # 한 칸 이동

            if not is_valid(ny, nx) or is_king(ny, nx):
                continue

            for j in range(2): # 대각선
                nny, nnx = ny + two[i][j][0], nx + two[i][j][1] # 한 번 이동
                if is_valid(nny, nnx) and not is_king(nny, nnx):
                    nny += two[i][j][0] # 두 번 이동
                    nnx += two[i][j][1]
                    if is_king(nny, nnx):
                        return count + 1
                    if is_valid(nny, nnx) and not visited[nny][nnx]:
                        visited[nny][nnx] = True
                        queue.append((nny, nnx, count + 1))

    return -1
print(bfs(sang[0], sang[1]))
