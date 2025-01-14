import sys
from collections import deque
N, L = map(int, sys.stdin.readline().strip().split())
array = list(map(int, sys.stdin.readline().strip().split()))
queue = deque()

for i in range(N):
    if queue and queue[0][0] <= i - L:
        queue.popleft()

    while len(queue) >= 1 and array[i] < queue[-1][1]:
        queue.pop()

    queue.append((i, array[i]))

    print(queue[0][1], end=' ')