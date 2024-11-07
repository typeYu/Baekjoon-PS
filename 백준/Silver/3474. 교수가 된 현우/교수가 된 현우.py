import sys
N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline().strip())
    count = 0
    i = 5
    while True:
        if num // i == 0:
            break
        count += num // i
        i *= 5
    print(count)