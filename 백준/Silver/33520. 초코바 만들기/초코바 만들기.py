import sys
input = sys.stdin.readline

n = int(input())
max_w = max_h = 0

for _ in range(n):
    a, b = map(int, input().split())
    w, h = sorted((a, b))
    max_w = max(max_w, w)
    max_h = max(max_h, h)

print(max_w * max_h)