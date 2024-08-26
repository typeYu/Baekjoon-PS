import sys
N = sys.stdin.readline().strip()
if '0' not in N:
    print(-1)
else:
    sumS = 0
    for i in range(len(N)):
        sumS += int(N[i])
    if sumS % 3 == 0:
        N = list(N)
        N.sort(reverse=True)
        print("".join(N))
    else:
        print(-1)
