import sys
N = int(sys.stdin.readline().rstrip())
dic = {}
for _ in range(N):
    word, extension = sys.stdin.readline().rstrip().split('.')
    if extension in dic:
        dic[extension] += 1
    else:
        dic[extension] = 1
dic = sorted(dic.items(), key=lambda x:x[0])
for i in dic:
    print(*i)