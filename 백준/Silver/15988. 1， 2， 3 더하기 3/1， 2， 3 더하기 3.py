import sys
T = int(input())
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    d = [0] * 1000000
    d[0] = 1
    d[1] = 2
    d[2] = 4
    for i in range(3, N):
        d[i] = (d[i - 1] + d[i - 2] + d[i - 3]) % 1000000009
    print(d[N - 1])