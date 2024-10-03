# 최대공약수가 1인 두 점을 찾으면 된다
from math import gcd
d = [0] * 1001
d[1] = 3
for i in range(2, 1001):
    for j in range(1, i):
        if gcd(i, j) == 1: # *2 해주고 전거랑 더해줘야
            d[i] += 2
    d[i] += d[i - 1]

for _ in range(int(input())):
    num = int(input())
    print(d[num])