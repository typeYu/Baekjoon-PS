import sys
N, M = map(int, sys.stdin.readline().strip().split())
money = []
for _ in range(M):
    money.append(int(sys.stdin.readline().strip()))
money.sort(reverse=True)

max_total = 0
num = 0
for i in range(1, M + 1):
    if money[i - 1] * i > max_total:
        if i <= N:
            max_total = money[i - 1] * i
            num = money[i - 1]

print(num, max_total, end='')