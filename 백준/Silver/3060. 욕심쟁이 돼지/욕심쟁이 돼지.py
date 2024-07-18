import sys
for _ in range(int(sys.stdin.readline().rstrip())):
    N = int(sys.stdin.readline().rstrip())
    pigs = sum(list(map(int, sys.stdin.readline().rstrip().split())))
    days = 1

    while True:
        if N - pigs < 0:
            print(days)
            break
        else:
            days += 1
            pigs *= 4