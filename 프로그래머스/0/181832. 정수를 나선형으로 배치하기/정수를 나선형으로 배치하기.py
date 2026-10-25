def solution(n):
    answer = [[0] * n for _ in range(n)]
    answer[0][0] = 1
    y, x = 0, 0
    loc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    num, d = 2, 0
    cnt = 1
    
    while cnt < n ** 2:
        ny, nx = y + loc[d][0], x + loc[d][1]
        if 0 <= ny < n and 0 <= nx < n and answer[ny][nx] == 0:
            answer[ny][nx] = num
            num += 1
            y, x = ny, nx
            cnt += 1
        else:
            d = (d + 1) % 4
    
    return answer