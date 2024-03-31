import sys
N = int(sys.stdin.readline().strip())
dic = {}
for _ in range(N):
    a = int(sys.stdin.readline().strip())
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1
RealDic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
print(RealDic[0][0])