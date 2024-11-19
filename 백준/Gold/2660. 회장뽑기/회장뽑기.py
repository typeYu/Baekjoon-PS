N = int(input())
graph = [[float('inf')] * (N + 1) for _ in range(N + 1)]
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a][b] = 1
    graph[b][a] = 1

# 자기 자신 초기화
for i in range(1, N):
    graph[i][i] = 0

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

score_list = [0]
min_score = float('inf')
for i in range(1, N + 1): # 후보 번호
    score = 0
    for j in range(1, N + 1): # 점수
        if i == j:
            continue
        score = max(score, graph[i][j])
    min_score = min(min_score, score)
    score_list.append(score)

print(min_score, score_list.count(min_score))
for s in range(1, len(score_list)):
    if score_list[s] == min_score:
        print(s, end=' ')