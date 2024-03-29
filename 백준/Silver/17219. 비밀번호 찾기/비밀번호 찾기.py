import sys
N, M = map(int, input().split())
dic = {}
for _ in range(N):
    a, b = sys.stdin.readline().rstrip().split()
    dic[a] = b
for _ in range(M):
    c = sys.stdin.readline().rstrip()
    print(dic[c])
