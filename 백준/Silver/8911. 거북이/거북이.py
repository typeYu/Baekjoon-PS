T = int(input())
dy = [-1, 0, 1, 0] # 상, 좌, 하, 우
dx = [0, -1, 0, 1]

for _ in range(T):
    S = input()
    turtle_y, turtle_x = 0, 0 # 현재 거북이 위치
    current_direction = 0 # 현재 거북이가 바라보고 있는 방향
    min_y, min_x, max_y, max_x = 0, 0, 0, 0 # 움직인 영역

    for s in S:
        if s == 'F':
            turtle_y += dy[current_direction]
            turtle_x += dx[current_direction]
        elif s == 'B':
            turtle_y -= dy[current_direction]
            turtle_x -= dx[current_direction]
        elif s == 'L':
            current_direction = (current_direction + 1) % 4
        elif s == 'R':
            current_direction = (current_direction + 3) % 4

        if s == 'F' or s == 'B':
            min_y, max_y = min(min_y, turtle_y), max(max_y, turtle_y)
            min_x, max_x = min(min_x, turtle_x), max(max_x, turtle_x)

    print((max_y - min_y) * (max_x - min_x))
    