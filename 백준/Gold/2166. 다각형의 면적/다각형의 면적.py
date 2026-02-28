import sys
x = []
y = []
N = int(sys.stdin.readline())
for _ in range(N):
    x1, y1 = map(int, sys.stdin.readline().strip().split())
    x.append(x1)
    y.append(y1)
x.append(x[0])
y.append(y[0])

answer = 0
for i in range(N):
    answer += x[i] * y[i + 1] - x[i + 1] * y[i]

print(abs(answer) * 0.5)