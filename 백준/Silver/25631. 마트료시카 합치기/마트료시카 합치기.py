import sys
N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().strip().split()))
dic = {}
for a in array:
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1

print(max(dic.values()))