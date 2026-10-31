from collections import deque

def solution(maps):
    H, W = len(maps), len(maps[0])
    start = [-1, -1]
    for i in range(H):
        for j in range(W):
            if maps[i][j] == "S":
                start = [i, j]
                break
    
    queue = deque([start + [0, 0]]) # able, count
    visited = [[False] * W for _ in range(H)]
    visited[start[0]][start[1]] = True

    while queue:
        y, x, able, cnt = queue.popleft()
        
        if maps[y][x] == "E" and able == 1:
            return cnt
        
        if maps[y][x] == "L":
            queue.clear()
            able = 1
            visited = [[False] * W for _ in range(H)]
            visited[y][x] = True
        
        for dy, dx in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < H and 0 <= nx < W and maps[ny][nx] != "X" and not visited[ny][nx]:
                queue.append([ny, nx, able, cnt + 1])
                visited[ny][nx] = True
    
    return -1
        