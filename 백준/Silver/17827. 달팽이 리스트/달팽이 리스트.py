import sys
N, M, V = map(int, sys.stdin.readline().strip().split())
array = list(map(int, sys.stdin.readline().strip().split()))
cycle = array[V - 1:]
for _ in range(M):
    K = int(sys.stdin.readline())
    if K < N:
        print(array[K])
    else:
        index = K - N
        index %= (N - V + 1)
        print(cycle[index])