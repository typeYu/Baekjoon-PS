def solution(park, routes):
    n, m = len(park), len(park[0])
    dic = {"E": (0, 1), "N": (-1, 0), "S": (1, 0), "W": (0, -1)}
    y, x = [0, 0]
    
    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':
                y, x = i, j
                break
    
    for r in routes:
        d, go = r.split(' ')
        go = int(go)
        dy, dx =  dic[d]
        for g in range(1, go + 1): # 몇 칸 가야 하나
            ny = y + g * dy
            nx = x + g * dx
            if 0 > ny or ny >= n or 0 > nx or nx >= m or park[ny][nx] == 'X':
                break
        else:
            y, x = y + go * dy, x + go * dx
    
    return [y, x]
            
    