N, M = map(int, input().split())
remain = 1

if N >= M:
    print(0)
else:
    for i in range(1, N + 1):
        remain *= i
        remain %= M

    print(remain)