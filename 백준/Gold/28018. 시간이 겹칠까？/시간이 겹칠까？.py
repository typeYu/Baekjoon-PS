import sys
N = int(sys.stdin.readline().strip())
d = [0] * 1000002
for _ in range(N):
    S, E = map(int, sys.stdin.readline().strip().split())
    d[S] += 1
    d[E + 1] -= 1 # 끝나는 시간에 좌석 선점 못함
Q = int(sys.stdin.readline().strip())
times = list(map(int, sys.stdin.readline().strip().split()))

prefix_sum = 0
for i in range(1, 1000001):
    prefix_sum += d[i]
    d[i] = prefix_sum

for t in times:
    print(d[t])