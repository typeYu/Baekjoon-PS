import sys
N = int(input())
T = []
P = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    T.append(a)
    P.append(b)

d = [0] * (N + 1)
for i in range(N):
    for j in range(i + 1): # 처음에 풀 때 이부분 빼먹음 조심 #
        if i + T[i] <= N:
            d[i + T[i]] = max(d[i + T[i]], d[j] + P[i])

print(max(d))