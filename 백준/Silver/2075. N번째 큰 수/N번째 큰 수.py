import sys
import heapq
N = int(sys.stdin.readline())
hq = []
length = 0 # 우선순위큐 길이
for _ in range(N):
    for num in list(map(int, sys.stdin.readline().strip().split())):
        if length < N:
            heapq.heappush(hq, num)
            length += 1
        else:
            if hq[0] < num:
                heapq.heappop(hq)
                heapq.heappush(hq, num)

print(hq[0])