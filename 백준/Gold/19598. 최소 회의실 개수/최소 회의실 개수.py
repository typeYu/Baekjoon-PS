import sys
import heapq

N = int(sys.stdin.readline())
rooms = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().strip().split())
    heapq.heappush(rooms, [a, b])

result = []
for _ in range(N):
    start, end = heapq.heappop(rooms)
    for i in range(len(result)):
        if result[i] <= start:
            result[i] = end
            break
    else:
        result.append(end)

print(len(result))