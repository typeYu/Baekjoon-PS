from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    
    visited = [[False] * m for _ in range(n)]
    queue = deque([(0, 0, 0)]) # y, x, cnt
    visited[0][0] = True
    
    while queue:
        y, x, cnt = queue.popleft()
        if y == n - 1 and x == m - 1:
            return cnt + 1
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and maps[ny][nx] != 0:
                visited[ny][nx] = True
                queue.append((ny, nx, cnt + 1))
        
    return -1