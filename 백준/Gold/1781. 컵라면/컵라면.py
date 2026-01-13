import sys
import heapq

N = int(sys.stdin.readline())
queue = []
for _ in range(N):
    deadline, rameon = map(int, sys.stdin.readline().strip().split())
    queue.append((deadline, rameon))

queue.sort(key=lambda x: (x[0], -x[1]))

answer = []
for _ in range(N):
    d, r = heapq.heappop(queue)
    heapq.heappush(answer, r)
    if len(answer) > d:
        heapq.heappop(answer)

print(sum(answer))