import sys
from bisect import bisect_right
N = int(sys.stdin.readline().rstrip())
ink = list(map(int, sys.stdin.readline().rstrip().split()))
viscosity = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(len(ink)):
    a = bisect_right(viscosity, ink[i]) - i - 1
    print(a, end=' ')