N, K = map(int, input().split())
d = [False] * (N + 1)
count = 0
for i in range(2, N + 1):
    for j in range(i, N + 1, i):
        if not d[j]:
            d[j] = True
            count += 1
            if count == K:
                print(j)
                exit()