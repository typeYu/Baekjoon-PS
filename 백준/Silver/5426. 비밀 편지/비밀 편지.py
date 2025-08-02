import sys
for _ in range(int(sys.stdin.readline())):
    S = sys.stdin.readline().strip()
    N = int(len(S) ** 0.5) # 제곱근

    for i in range(N - 1, -1, -1):
        for j in range(i, len(S), N):
            print(S[j], end='')
    print()