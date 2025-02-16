# 그람을 얻은 후, 왔던 길을 다시 갈 수 있어야 한다. visited 외에 i_have_gram 배열로 추가 경로 설정
# grobal gram으로 관리하지 말 것. 한 경로에서 그람을 얻으면 모든 경로가 그람을 얻은 것으로 처리되어,
# 아직 그람을 획득하지 않은 경로에서도 벽을 부수는 이동을 허용하게 되어 버림

import sys
from collections import deque


def bfs():

    queue = deque([(0, 0, 0, False)]) # y좌표, x좌표, 시간, 그람 획득 여부
    visited[0][0] = 0
    while queue:
        y, x, time, gram = queue.popleft()
        if graph[y][x] == 2:
            gram = True

        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                if gram and i_have_gram[ny][nx] == INF:
                    i_have_gram[ny][nx] = time + 1
                    queue.append((ny, nx, time + 1, gram))
                else:
                    if visited[ny][nx] == INF and graph[ny][nx] != 1:
                        visited[ny][nx] = time + 1
                        queue.append((ny, nx, time + 1, gram))

    answer = min(i_have_gram[N - 1][M - 1], visited[N - 1][M - 1])
    if answer == INF or answer > T:
        return "Fail"
    else:
        return answer


N, M, T = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
INF = float('inf')
visited = [[INF] * M for _ in range(N)]
i_have_gram = [[INF] * M for _ in range(N)]

print(bfs())