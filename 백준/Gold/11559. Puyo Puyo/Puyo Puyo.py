from collections import deque
graph = []
for _ in range(12):
    graph.append(list(input()))

def bfs(i, j, S):
    queue = deque([(i, j)])
    visited = []

    while queue:
        y, x = queue.popleft()
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < 12 and 0 <= nx < 6 and (ny, nx) not in visited and graph[ny][nx] == S:
                queue.append((ny, nx))
                visited.append((ny, nx))

    if len(visited) >= 4:
        return visited
    else:
        return False

def gravity():
    global graph
    for i in range(10, -1, -1):
        for j in range(6):
            plus = 1
            if graph[i][j] != '.' and graph[i + plus][j] == '.':
                while True:
                    plus += 1
                    if i + plus >= 12 or graph[i + plus][j] != '.':
                        graph[i + plus - 1][j] = graph[i][j]
                        graph[i][j] = '.'
                        break

answer = 0
while True:
    is_pang = False
    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.':
                result = bfs(i, j, graph[i][j])
                if not result:
                    continue
                else:
                    for vy, vx in result:
                        graph[vy][vx] = '.'
                    is_pang = True

    if is_pang:
        gravity()
        answer += 1
        continue
    else:
        break

print(answer)