def solution(dirs):
    answer = 0
    loc = {"U":(1, 0), "D": (-1, 0), "R": (0, 1), "L": (0, -1)}
    y, x = 0, 0
    visited = set()
    
    for d in dirs:
        dy, dx = loc[d]
        ny, nx = y + dy, x + dx
        if -5 <= ny <= 5 and -5 <= nx <= 5:
            visited.add((y, x, ny, nx))
            visited.add((ny, nx, y, x))
            y, x = ny, nx

    return len(visited) // 2