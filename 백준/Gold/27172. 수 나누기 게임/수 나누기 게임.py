import sys
N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().strip().split()))
S = set(array)
M = max(array)
answer = [0] * (M + 1)
for i in array:
    for j in range(i * 2, M + 1, i):
        if j in S:
            answer[i] += 1
            answer[j] -= 1

for i in array:
    print(answer[i], end=' ')