import sys
N = int(sys.stdin.readline())
lines = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().strip().split())
    lines.append([x, y])

lines.sort(key=lambda x: x[0])

start, end = lines[0][0], lines[0][1]
result = 0
for x, y in lines: # 1. 완전히 속하는 경우 2. 일부 겹치는 경우 3. 아예 새로 시작하는 경우
    if start <= x <= end and start <= y <= end:
        continue
    elif start <= x <= end:
        end = y
    elif end < x:
        result += end - start
        start = x
        end = y

result += end - start
print(result)