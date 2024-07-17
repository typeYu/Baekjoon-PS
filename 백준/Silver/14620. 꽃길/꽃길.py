from itertools import combinations
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
result = {} # (꽃술 좌표): 가격
dy_dx = [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1)]
for i in range(1, N - 1): # 꽃술 위치
    for j in range(1, N - 1):
        money = 0 # 5평의 비용
        for dy, dx in dy_dx:
            ny, nx = i + dy, j + dx
            money += graph[ny][nx]
            result[(i, j)] = money

def error(y1, x1, y2, x2):
    if y1 == y2 and x1 == x2:
        return False
    if y1 == y2 and abs(x1 - x2) <= 2 or x1 == x2 and abs(y1 - y2) <= 2:
        return False
    if abs(y1 - y2) == 1 and abs(x1 - x2) == 1:
        return False
    return True

comb = combinations(result.items(), 3)

all_money = []
for a, b, c in comb:
    if error(a[0][0], a[0][1], b[0][0], b[0][1]) and error(a[0][0], a[0][1], c[0][0], c[0][1]) and error(b[0][0], b[0][1], c[0][0], c[0][1]):
        all_money.append(a[1] + b[1] + c[1])

print(min(all_money))