T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    floor = N % H
    ho = N // H + 1
    if floor == 0:
        floor = H
        ho = N // H
    print(floor * 100 + ho)