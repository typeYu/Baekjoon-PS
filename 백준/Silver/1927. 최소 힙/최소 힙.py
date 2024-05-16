import heapq
import sys
N = int(sys.stdin.readline().rstrip())
heap = []
heapq.heapify(heap)
for _ in range(N):
    a = int(sys.stdin.readline().rstrip())
    if a == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, a)
