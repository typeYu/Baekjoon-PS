from collections import deque
T = int(input())

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 1 # 처음 좌표 방문처리 해주기
    while queue:
        x, y = queue.popleft()
        if x == moveX and y == moveY:
            return visited[moveX][moveY]

        for dx, dy in [(-1, 2), (-2, 1), (2, 1), (1, 2), (1, -2), (2, -1), (-2, -1), (-1, -2)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < l and 0 <= ny < l and visited[nx][ny] == 0:
                queue.append((nx, ny)) # 탐색한 좌표 큐에 넣어줘야
                visited[nx][ny] = visited[x][y] + 1

for _ in range(T):
    l = int(input())
    array = [[0] * l for _ in range(l)]
    visited = [[0] * l for _ in range(l)]
    currentX, currentY = map(int, input().split())
    moveX, moveY = map(int, input().split())
    print(bfs(currentX, currentY) - 1)