#round 쓰면 통과 안됨
import sys
dic = {}
while True:
    tree = sys.stdin.readline().rstrip()
    if not tree:
        break
    if tree in dic:
        dic[tree] += 1
    else:
        dic[tree] = 1
total = sum(dic.values())
dicS = sorted(dic.items(), key=lambda x: x[0])
for i in dicS:
    print(i[0], f"{int(i[1]) / total * 100:.4f}")