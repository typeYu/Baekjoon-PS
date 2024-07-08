while True:
    N = int(input())
    if N == 0:
        break
    else:
        d = []
        for _ in range(N):
            d.append(int(input()))

        for i in range(1, len(d)):
            d[i] = max(d[i], d[i - 1] + d[i])
        print(max(d))