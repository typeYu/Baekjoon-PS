import sys
from math import gcd
for _ in range(int(sys.stdin.readline())):
    array = list(map(int, sys.stdin.readline().strip().split()))
    N = array[0]
    array = array[1:]
    answer = 0
    for i in range(N):
        for j in range(i + 1, N):
            answer += gcd(array[i], array[j])

    print(answer)