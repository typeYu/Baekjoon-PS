N, M = map(int, input().split())
graph = [[float('inf')] * N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1

for i in range(N):
    graph[i][i] = 0

for k in range(N):
    for a in range(N):
        for b in range(N):
            if graph[a][b] == 1 or (graph[a][k] == 1 and graph[k][b] == 1):
                graph[a][b] = 1 # a부터 b까지 갈 수만 있으면 1(거리 고려 x)

result = 0 # 총 결괏값
for i in range(N):
    count = 0 # 0부터 N - 1번 인덱스까지 몇명의 사람과 이어져 있는지 카운트
    for j in range(N):
        if graph[i][j] == 1 or graph[j][i] == 1: # 거리, 방향 고려 없이 일단 경로가 존재하면
            count += 1 # 방향 그래프라서 도달할 수 없으면 count 되지 않음

    if count == N - 1: # 모든 노드들과 경로를 공유하고 있으면
        result += 1

print(result)