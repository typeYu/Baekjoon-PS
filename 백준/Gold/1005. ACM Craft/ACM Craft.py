import sys
from collections import deque


def topology_sort():
    dp = [0] * (N + 1)  # 건물마다 걸리는 최소 시간 기록

    queue = deque()
    for city in range(1, N + 1):
        if inDegree[city] == 0:
            queue.append(city)
            dp[city] = D[city]

    while queue:
        q = queue.popleft()
        if q == W:
            return dp[q]

        for g in graph[q]: # 선행 작업 진행 중 (하위 작업 inDegree 하나씩 해제)
            inDegree[g] -= 1
            dp[g] = max(dp[g], dp[q] + D[g]) # ** 중요 ** 작업 진행 될 때마다 dp 갱신하면서 선행 작업이 끝날 때까지의 시간을 구함
            if inDegree[g] == 0:
                queue.append(g)


for _ in range(int(sys.stdin.readline())):
    N, K = map(int, sys.stdin.readline().strip().split())
    D = list(map(int, sys.stdin.readline().strip().split()))
    D.insert(0, 0)
    graph = [list() for _ in range(N + 1)]
    inDegree = [0] * (N + 1)
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().strip().split())
        graph[X].append(Y)
        inDegree[Y] += 1

    W = int(sys.stdin.readline().strip())

    print(topology_sort())