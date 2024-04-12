import sys
N, C = map(int, input().split())
array = map(int, sys.stdin.readline().rstrip().split())
dic = {}
for i in array:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
sortedDic = sorted(dic.items(), key=lambda x: -x[1])
for i, j in sortedDic:
    print(f"{i} " * j, end="")