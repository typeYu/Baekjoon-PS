import sys
from collections import deque


def bfs(entrance, wait, answer):
    global graph
    visited = [[False] * w for _ in range(h)]
    queue = deque(entrance)

    while queue:
        y, x = queue.popleft()
        if graph[y][x] in uppercase and uppercase[graph[y][x]] != 1:
            # 열쇠가 없으면 대기
            wait.append((graph[y][x], y, x))
        else:
            for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ny, nx = y + dy, x + dx
                if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx] and graph[ny][nx] != '*':
                    visited[ny][nx] = True
                    if graph[ny][nx] == '.':
                        queue.append((ny, nx))
                    elif graph[ny][nx] == '$':
                        answer.add((ny, nx))
                        queue.append((ny, nx))
                    elif graph[ny][nx] in lowercase:
                        visited = [[False] * w for _ in range(h)]
                        # 새로운 열쇠 발견
                        uppercase[chr(ord(graph[ny][nx]) - 32)] = 1
                        graph[ny][nx] = '.'
                        queue.append((ny, nx))

                        # 새로운 열쇠로 대기 중인 문 처리
                        new_wait = []
                        for wa in wait:
                            if uppercase[wa[0]] == 1:
                                queue.append((wa[1], wa[2]))
                                graph[wa[1]][wa[2]] = '.'
                            else:
                                new_wait.append(wa)
                        wait = new_wait
                    elif graph[ny][nx] in uppercase:
                        if uppercase[graph[ny][nx]] == 1:
                            # 문을 열 수 있는 경우
                            graph[ny][nx] = '.'
                            queue.append((ny, nx))
                        else:
                            # 열쇠가 없으면 대기
                            wait.append((graph[ny][nx], ny, nx))

    return len(answer)


for _ in range(int(sys.stdin.readline())):
    h, w = map(int, sys.stdin.readline().strip().split())
    graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(h)]
    key_list = list(sys.stdin.readline().strip())
    entrance, wait = [], []
    uppercase = {chr(i): 0 for i in range(ord('A'), ord('Z') + 1)}
    lowercase = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
    answer = set()

    if key_list[0] != "0":
        for k in key_list:
            uppercase[chr(ord(k) - 32)] = 1

    for i in range(h):
        if graph[i][0] != '*':
            if graph[i][0] in lowercase:
                uppercase[chr(ord(graph[i][0]) - 32)] = 1
                graph[i][0] = '.'
            elif graph[i][0] in uppercase and uppercase[graph[i][0]] == 0:
                wait.append((graph[i][0], i, 0))  # 열쇠가 없는 문
            elif graph[i][0] == '$':
                answer.add((i, 0))
            entrance.append((i, 0))

        if graph[i][w - 1] != '*':
            if graph[i][w - 1] in lowercase:
                uppercase[chr(ord(graph[i][w - 1]) - 32)] = 1
                graph[i][w - 1] = '.'
            elif graph[i][w - 1] in uppercase and uppercase[graph[i][w - 1]] == 0:
                wait.append((graph[i][w - 1], i, w - 1))
            elif graph[i][w - 1] == '$':
                answer.add((i, w - 1))
            entrance.append((i, w - 1))

    for i in range(1, w - 1):
        if graph[0][i] != '*':
            if graph[0][i] in lowercase:
                uppercase[chr(ord(graph[0][i]) - 32)] = 1
                graph[0][i] = '.'
            elif graph[0][i] in uppercase and uppercase[graph[0][i]] == 0:
                wait.append((graph[0][i], 0, i))
            elif graph[0][i] == '$':
                answer.add((0, i))
            entrance.append((0, i))

        if graph[h - 1][i] != '*':
            if graph[h - 1][i] in lowercase:
                uppercase[chr(ord(graph[h - 1][i]) - 32)] = 1
                graph[h - 1][i] = '.'
            elif graph[h - 1][i] in uppercase and uppercase[graph[h - 1][i]] == 0:
                wait.append((graph[h - 1][i], h - 1, i))
            elif graph[h - 1][i] == '$':
                answer.add((h - 1, i))
            entrance.append((h - 1, i))

    print(bfs(entrance, wait, answer))


