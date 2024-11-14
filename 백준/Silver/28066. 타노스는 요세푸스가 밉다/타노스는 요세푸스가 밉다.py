import sys
from collections import deque
N, K = map(int, sys.stdin.readline().strip().split())
queue = deque([i for i in range(1, N + 1)])
while len(queue) >= K:
    first = queue.popleft()
    for i in range(K - 1):
        queue.popleft()
    queue.append(first)

print(queue[0])