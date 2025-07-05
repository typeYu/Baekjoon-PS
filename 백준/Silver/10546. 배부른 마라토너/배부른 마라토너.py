import sys
input = sys.stdin.readline

n = int(input().rstrip())
dic = {}
for i in range(n):
    s = input().rstrip()
    if s not in dic:
        dic[s] = 1
    else: # 동명이인 가능
        dic[s] += 1

for i in range(n-1):
    s = input().rstrip()
    dic[s] -= 1 # 완주한 이름은 -1

for key, value in dic.items():
    if value != 0: # 아직 남아있다면
        print(key)
        break