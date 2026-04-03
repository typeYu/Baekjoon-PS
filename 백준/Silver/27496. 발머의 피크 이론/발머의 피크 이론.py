import sys
N, L = map(int, sys.stdin.readline().split())
alcohol = list(map(int, sys.stdin.readline().split()))
total = 0
answer = 0

for i in range(N):
    if i < L:
        total += alcohol[i]
        if 129 <= total <= 138:
            answer += 1
    else:
        total -= alcohol[i - L]
        total += alcohol[i]
        if 129 <= total <= 138:
            answer += 1
print(answer)