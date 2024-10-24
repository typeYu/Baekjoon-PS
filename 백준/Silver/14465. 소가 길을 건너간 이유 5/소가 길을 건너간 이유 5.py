import sys
N, K, B = map(int, sys.stdin.readline().strip().split())
light = [1] * N
for _ in range(B):
    light[int(sys.stdin.readline()) - 1] = 0

prefix_sum = sum(light[:K])
need = K - prefix_sum
start = 0
for end in range(K, N):
    if light[start] == 1:
        prefix_sum -= 1
    if light[end] == 1:
        prefix_sum += 1
    need = min(need, K - prefix_sum)
    start += 1

print(need)