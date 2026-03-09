import sys
N, M, K = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
people = [0 for _ in range(N)]

for j in range(M):
    for i in range(N):
        people[i] += graph[i][j]
        if people[i] >= K:
            print(i + 1, j + 1)
            exit()