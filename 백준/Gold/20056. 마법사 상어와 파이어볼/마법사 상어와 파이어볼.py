import sys
N, M, K = map(int, sys.stdin.readline().strip().split())
fireballs = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]
direction = {0: [-1, 0], 1: [-1, 1], 2: [0, 1], 3: [1, 1], 4: [1, 0], 5: [1, -1], 6: [0, -1], 7: [-1, -1]}

def m_is(arr): # 질량은
    return sum(arr) // 5

def s_is(arr): # 속력은
    return sum(arr) // len(arr)

def direction_is(arr):
    even, odd = 0, 0
    for a in arr:
        if a % 2 == 0:
            even += 1
        else:
            odd += 1

    return [0, 2, 4, 6] if even == 0 or odd == 0 else [1, 3, 5, 7]

def move():
    global fireballs

    Map = [[[] for _ in range(N)] for _ in range(N)]

    for fireball in fireballs:
        y, x = fireball[0] - 1, fireball[1] - 1
        m, s, d = fireball[2], fireball[3], fireball[4] # 질량, 속력, 방향

        dy, dx = direction[d][0] * s, direction[d][1] * s
        ny, nx = (y + dy) % N, (x + dx) % N
        Map[ny][nx].append([m, s, d])

    new_fireballs = []

    for i in range(N):
        for j in range(N):
            # 파이어볼 한개일 땐 그대로
            if len(Map[i][j]) == 1:
                m, s, d = Map[i][j][0]
                new_fireballs.append([i + 1, j + 1, m, s, d]) # fireballs에 넣을 때 인덱스 조심
            elif len(Map[i][j]) >= 2:
                ms, ss, ds = [], [], []
                for a, b, c in Map[i][j]:
                    ms.append(a)
                    ss.append(b)
                    ds.append(c)
                new_m = m_is(ms)
                new_s = s_is(ss)
                new_d = direction_is(ds)

                if new_m > 0:
                    for d in new_d:
                        new_fireballs.append([i + 1, j + 1, new_m, new_s, d]) # fireballs에 넣을 때 인덱스 조심

    fireballs = new_fireballs


for _ in range(K):
    move()

answer = 0
if len(fireballs) > 0:
    for y, x, m, s, d in fireballs:
        answer += m

print(answer)