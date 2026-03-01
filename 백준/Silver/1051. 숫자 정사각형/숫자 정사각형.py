import sys
N, M = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

answer = 1

for i in range(N):
    for j in range(M):
        plus = 1
        start = graph[i][j] # 맨 왼쪽 위 꼭지점 수
        while True:
            if i + plus >= N or j + plus >= M:
                break

            if start == graph[i + plus][j] == graph[i][j + plus] == graph[i + plus][j + plus]:
                answer = max(answer, (plus + 1) ** 2)

            plus += 1

print(answer)