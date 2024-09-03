import heapq

N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
s_y, s_x = 0, 0
f_y, f_x = 0, 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 'S':
            s_y, s_x = i, j
        elif graph[i][j] == 'F':
            f_y, f_x = i, j
        elif graph[i][j] == 'g':
            for y, x in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ny, nx = i + y, j + x
                if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] not in ('S', 'F', 'g'):
                    graph[ny][nx] = 'a'  # 쓰레기가 인접한다는 뜻

visited = [[False] * M for _ in range(N)]


def bfs(y, x):
    queue = [(0, 0, y, x)]  # 쓰레기 수, 쓰레기 인접 칸 수, y 좌표, x 좌표
    heapq.heapify(queue)
    visited[y][x] = True

    while queue:
        garb, adja, y, x = heapq.heappop(queue)
        if y == f_y and x == f_x:
            return (garb, adja)

        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                visited[ny][nx] = True  # 방문 처리 위치 수정
                if graph[ny][nx] == 'g':
                    heapq.heappush(queue, (garb + 1, adja, ny, nx))
                elif graph[ny][nx] == 'a':
                    heapq.heappush(queue, (garb, adja + 1, ny, nx))
                else:
                    heapq.heappush(queue, (garb, adja, ny, nx))


print(*bfs(s_y, s_x))
