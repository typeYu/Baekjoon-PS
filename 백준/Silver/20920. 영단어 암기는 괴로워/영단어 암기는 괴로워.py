import sys
N, M = map(int, input().split())
dic = {}
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) < M:
        continue
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1
a = sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for i in a:
    print(i[0])