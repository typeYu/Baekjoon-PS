from collections import deque
N, K = map(int, input().split())
visited = [0 for _ in range(100001)]
dic = {} # 전 인덱스 저장할 딕셔너리
result = [] # 결과 출력 할 스택

def bfs(N):
    queue = deque([N])
    visited[N] = 1
    dic[N] = N
    while queue:
        q = queue.popleft()
        if q == K:
            print(visited[q] - 1)
            idx = K
            for _ in range(visited[q]):
                result.append(idx)
                idx = dic[idx]
            result.reverse()
            for i in range(len(result)):
                print(result[i], end=' ')
            break
        for dn in [q + 1, q - 1, 2 * q]:
            if 0 <= dn < 100001 and visited[dn] == 0:
                visited[dn] = visited[q] + 1
                dic[dn] = q
                queue.append(dn)

bfs(N)