import sys
L, N = map(int, sys.stdin.readline().strip().split())
S = [sys.stdin.readline().strip() for _ in range(N)]
K = int(sys.stdin.readline())

dic = dict()

for i in range(N):
    for j in range(L - K + 1):
        s = S[i][j:j + K]
        if s not in dic:
            dic[s] = 1
        else:
            dic[s] += 1

print(max(dic.values()))