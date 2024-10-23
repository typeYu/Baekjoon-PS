import sys
import heapq
N = int(sys.stdin.readline())
array = []
for _ in range(N):
    s, t = map(int, sys.stdin.readline().strip().split())
    array.append([s, t])
array.sort()
heapq.heapify(array)

last = []
heapq.heapify(last)

while array:
    start, end = heapq.heappop(array)
    if len(last) == 0:
        heapq.heappush(last, end)
        continue
    else:
        last_end = heapq.heappop(last)
        if last_end > start:
            heapq.heappush(last, end)
            heapq.heappush(last, last_end)
        else:
            heapq.heappush(last, end)

print(len(last))