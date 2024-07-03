import sys
N = int(input())
dic = {}
for _ in range(N):
    a = list(sys.stdin.readline().rstrip())
    if a[0] in dic:
        dic[a[0]] += 1
    else:
        dic[a[0]] = 1
result = []
for key, val in dic.items():
    if val >= 5:
        result += key
result.sort()
if result:
    for i in result:
        print(i, end='')
else:
    print("PREDAJA")