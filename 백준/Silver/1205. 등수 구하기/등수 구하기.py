import sys
N, ts, P = map(int, sys.stdin.readline().strip().split())

if N == 0:
    print(1)
else:
    rank = list(map(int, sys.stdin.readline().strip().split()))
    if N == P and rank[-1] >= ts:
        print(-1)
    else:
        result = N + 1
        for i in range(N):
            if rank[i] <= ts:
                result = i + 1
                break
        print(result)