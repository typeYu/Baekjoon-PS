from collections import deque
N, M = map(int, input().split())
stair, snake = {}, {}
for _ in range(N):
    a, b = map(int, input().split())
    stair[a] = b
for _ in range(M):
    a, b = map(int, input().split())
    snake[a] = b


def bfs(num):
    visited = [-1] * 101
    count = 0
    queue = deque([(num, count)])
    visited[num] = count

    while queue:
        q, count = queue.popleft()
        if q == 100:
            return visited[q]

        for nq in [q + 1, q + 2, q + 3, q + 4, q + 5, q + 6]:
            # 방문한 칸에 사다리나 뱀이 있을 시 count나 visit을 판단하여 타는지 여부를 파악하면 안되고
            # 사다리나 뱀이 있으면 무조건 일단 사다리나 뱀이 가리키는 방향으로 가야
            if nq < 101:
                if nq in stair:
                    nq = stair[nq]
                elif nq in snake:
                    nq = snake[nq]
            #############################
                if visited[nq] == -1:
                    queue.append((nq, count + 1))
                    visited[nq] = count + 1

print(bfs(1))