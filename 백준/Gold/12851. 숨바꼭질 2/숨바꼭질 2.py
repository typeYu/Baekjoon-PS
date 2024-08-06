from collections import deque
N, K = map(int, input().split())
visited = [0 for _ in range(100001)]


def bfs(N):
    quick_time, count = 0, 0
    queue = deque([N])
    visited[N] = 1
    while queue:
        q = queue.popleft()
        if q == K:
            quick_time = visited[q] - 1
            count += 1

        for dn in [q + 1, q - 1, q * 2]:
            # visited[dn] == visited[q] + 1인 경우를 추가해준다
            # 만약 4에서 6까지 가는 방법이 2개 있을 때, 5에서 6까지 가는 경우를 이미 계산했다고 치면
            # visited[6] = 3이다.(2번만에 갔으므로)
            # 이 때 q는 3이고 dn이 6인 경우 visited[3] = 2로(1번만에 감)
            # visited = 0은 아니지만 visited[6] == visited[3] + 1임
            if 0 <= dn < 100001 and (visited[dn] == 0 or visited[dn] == visited[q] + 1):
                visited[dn] = visited[q] + 1
                queue.append(dn)

    print(quick_time, count, sep='\n')

bfs(N)