import sys
N, K = map(int, input().split())
S = list(map(int, sys.stdin.readline().strip().split()))
D = list(map(int, sys.stdin.readline().strip().split()))
num = 0
while K > num:
    P = [0] * N
    for i in range(N):
        P[D[i] - 1] = S[i]
    S = P
    num += 1
for i in S:
    print(i, end=' ')