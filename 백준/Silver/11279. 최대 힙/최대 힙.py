import heapq
import sys
N = int(input())
array = []
heapq.heapify(array)

for _ in range(N):
    i = int(sys.stdin.readline().strip())
    if i == 0:
        if len(array) == 0:
            print(0)
        else:
            print(heapq.heappop(array)[1])
    else:
        heapq.heappush(array, (-i, i))