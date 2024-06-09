import sys
N = int(sys.stdin.readline().rstrip())
T_shirts = list(map(int, sys.stdin.readline().rstrip().split()))
T, P = map(int, sys.stdin.readline().rstrip().split())

resultT = 0
for i in T_shirts:
    if i % T == 0:
        resultT += i // T
    else:
        resultT += i // T + 1
print(resultT)
resultP = N // P
each = N % P
print(resultP, each)