import sys
N, M = map(int, sys.stdin.readline().strip().split())
array = []
for i in range(N):
    array.append(int(sys.stdin.readline().strip()))
array.sort()

dic = {}
for i in range(N):
    if array[i] not in dic:
        dic[array[i]] = i

for _ in range(M):
    num = int(sys.stdin.readline().strip())
    if num in dic:
        print(dic[num])
    else:
        print(-1)