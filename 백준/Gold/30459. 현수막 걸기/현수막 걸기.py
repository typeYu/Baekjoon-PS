import sys
from itertools import combinations
N, M, R = map(int, sys.stdin.readline().strip().split())
base = list(map(int, sys.stdin.readline().strip().split()))
height = list(map(int, sys.stdin.readline().strip().split()))
all_base = set() # 두 말뚝 사이의 모든 거리를 구함
for a, b in combinations(base, 2):
    all_base.add(abs(a - b))

height.sort()

result = -1
for i in all_base:
    start, end = 0, len(height) - 1
    while start <= end:
        mid = (start + end) // 2
        area = (height[mid] * i) / 2
        if area == float(R):
            print(float(R))
            exit()
        elif area < float(R):
            start = mid + 1
        else:
            end = mid - 1
    if (height[end] * i) / 2 <= R:
        result = max(result, (height[end] * i) / 2)

if result == -1:
    print(-1)
else:
    print(f"{result:.1f}")