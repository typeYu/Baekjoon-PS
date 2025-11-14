import sys


def init_floyd():
    for i in range(1, N + 1):
        graph[i][i] = 0

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


def floyd(a1, b1, c1, a2, b2, c2):
    # s에서 a1 + c1 + b1에서 T를 직접 구할 것

    # 여기서 바로 3중 for문 하면 안되고 경로를 하나만 구하면 됨
    # for k in range(1, N + 1):
    #     for i in range(1, N + 1):
    #         for j in range(1, N + 1):
    #             temp_graph[i][j] = min(temp_graph[i][j], temp_graph[i][k] + temp_graph[k][j])

    ans1 = graph[S][a1] + c1 + graph[b1][T]
    ans2 = graph[S][a2] + c2 + graph[b2][T]
    ans3 = graph[S][T]
    ans4 = graph[S][a1] + c1 + graph[b1][a2] + c2 + graph[b2][T]
    ans5 = graph[S][a2] + c2 + graph[b2][a1] + c1 + graph[b1][T]

    return min(ans1, ans2, ans3, ans4, ans5)


N, M, S, T = map(int, sys.stdin.readline().strip().split())
graph = [[float('inf')] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().strip().split())
    graph[u][v] = min(graph[u][v], w)

init_floyd()

Q = int(sys.stdin.readline())
for _ in range(Q):
    a1, b1, c1, a2, b2, c2 = map(int, sys.stdin.readline().strip().split())
    answer = min(float('inf'), floyd(a1, b1, c1, a2, b2, c2))

    if answer == float('inf'):
        print(-1)
    else:
        print(answer)
