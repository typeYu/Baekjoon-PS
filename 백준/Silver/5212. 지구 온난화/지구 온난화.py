import sys

def melt(y, x):
    cnt = 0
    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ny, nx = y + dy, x + dx
        if graph[ny][nx] == '.':
            cnt += 1

    if cnt >= 3:
        return False

    return True

R, C = map(int, sys.stdin.readline().strip().split())
graph = [['.'] * (C + 2)]
for _ in range(R):
    graph.append(['.'] + list(sys.stdin.readline().strip()) + ['.'])
graph.append(['.'] * (C + 2))

queue = []
for y in range(R + 2):
    for x in range(C + 2):
        if graph[y][x] == 'X':
            queue.append((y, x))

answer = []
for y, x in queue:
    if melt(y, x):
        answer.append([y, x])

max_x, min_x = 0, float('inf')
max_y, min_y = 0, float('inf')

graph = [['.'] * (C + 2) for _ in range(R + 2)]
for y, x in answer:
    graph[y][x] = 'X'
    max_x = max(max_x, x)
    min_x = min(min_x, x)
    max_y = max(max_y, y)
    min_y = min(min_y, y)

for i in range(min_y, max_y + 1):
    print(''.join(map(str, graph[i][min_x:max_x + 1])))
