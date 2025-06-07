import heapq
import sys
N, H, T = map(int, sys.stdin.readline().strip().split())
queue = []
for _ in range(N):
    heapq.heappush(queue, -int(sys.stdin.readline()))

for i in range(T):
    num = -heapq.heappop(queue)
    if num < H:
        print("YES")
        print(i)
        exit()
    else:
        change_num = int(num / 2)
        if change_num < 1:
            change_num = 1
        heapq.heappush(queue, -change_num)

last = -(heapq.heappop(queue))
if H <= last:
    print("NO")
    print(last)
else:
    print("YES")
    print(T)