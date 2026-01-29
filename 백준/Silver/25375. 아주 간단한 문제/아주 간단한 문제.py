import sys
for _ in range(int(sys.stdin.readline())):
    a, b = map(int, input().split())
    if b % a == 0 and b//a >= 2: print(1)
    else: print(0)