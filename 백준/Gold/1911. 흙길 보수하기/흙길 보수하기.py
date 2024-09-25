import sys
N, L = map(int, sys.stdin.readline().strip().split())
lines = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().strip().split())
    lines.append([x, y])

lines.sort(key=lambda x: x[0])

end = 0
result = 0
for x, y in lines:
    if end <= x:
        if y - x >= L and (y - x) % L == 0:
            result += (y - x) // L
            end = y
        else:
            result += (y - x) // L + 1
            end = x + ((y - x) // L + 1) * L
    else:
        if end >= y:
            continue
        else:
            if y - end >= L and (y - end) % L == 0:
                result += (y - end) // L
                end = y
            else:
                result += (y - end) // L + 1
                end = end + ((y - end) // L + 1) * L

print(result)