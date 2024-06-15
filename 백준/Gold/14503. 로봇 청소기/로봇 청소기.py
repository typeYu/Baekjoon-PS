N, M = map(int, input().split())
r, c, d = map(int, input().split())
dx = [-1, 0, 1, 0] # 북, 동, 남, 서
dy = [0, 1, 0, -1]
graph = [list(map(int, input().split())) for _ in range(N)]

def isClean(x, y): # 상하좌우 청소가 되어있는지. True면 전부 청소(전부 1)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0: # **** 범위 설정 잊어버리지 않기
            return False
    return True

def robot(x, y):
    global d
    count = 0 # 청소 횟수

    while True:
        if graph[x][y] == 0:
            graph[x][y] = 2 # 청소 완료
            count += 1

        if not isClean(x, y): # 4칸 중 청소되지 않은 빈 칸이 있는 경우
            for _ in range(4): # 반시계 방향 회전
                d = (d + 3) % 4
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                    x = nx
                    y = ny
                    break
        else:
            nx = x - dx[d]
            ny = y - dy[d]
            if not 0 <= nx < N or not 0 <= ny < M or graph[nx][ny] == 1:
                break
            x, y = nx, ny
    return count

print(robot(r, c))


# 7 7
# 4 2 1
# 1 1 1 1 1 1 1
# 1 0 0 0 1 0 1
# 1 0 1 1 0 0 1
# 1 0 0 0 0 1 1
# 1 0 0 1 0 0 1
# 1 0 0 0 0 0 1
# 1 1 1 1 1 1 1