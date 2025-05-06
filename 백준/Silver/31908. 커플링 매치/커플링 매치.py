import sys
N = int(sys.stdin.readline())
dic = {}
for _ in range(N):
    name, ring = map(str, sys.stdin.readline().strip().split())
    if ring == '-':
        continue
    if ring not in dic:
        dic[ring] = [name]
    else:
        dic[ring].append(name)

cnt_couple = 0
couple = []
for people in dic.values():
    if len(people) == 2:
        cnt_couple += 1
        couple.append(people)

print(cnt_couple)
for c in couple:
    print(*c)