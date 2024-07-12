import sys
N = int(sys.stdin.readline().rstrip())
robots = []
for i in range(1, N + 1):
    x, y, speed = map(int, sys.stdin.readline().rstrip().split())
    robots.append((((x**2 + y**2) ** 0.5) / speed, i))

robots.sort(key=lambda x: (x[0], x[1]))

for r in robots:
    print(r[1])
