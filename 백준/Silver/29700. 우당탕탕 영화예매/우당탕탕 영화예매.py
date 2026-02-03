import sys
N, M, K = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

if K > M:
    print(0)
    exit()

answer = 0
for i in range(N):
    cnt = 0
    for j in range(M - K + 1):
        if j == 0:
            cnt = graph[i][:K].count(0)
            if cnt == K:
                answer += 1
        else:
            if graph[i][j - 1] == 0:
                cnt -= 1
            if graph[i][j + K - 1] == 0:
                cnt += 1

            if cnt == K:
                answer += 1

print(answer)