import sys
N = int(input())
goods = []
for _ in range(N):
    goods.append(int(sys.stdin.readline().strip()))

goods.sort(reverse=True)
result = 0
for i in range(1, len(goods) + 1):
    if i % 3 == 0:
        continue
    else:
        result += goods[i - 1]

print(result)