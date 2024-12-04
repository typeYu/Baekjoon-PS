import sys
from collections import deque
N = int(sys.stdin.readline())
array = deque([i for i in range(1, N + 1)])
while len(array) > 1:
    print(array.popleft(), end=' ')
    array.append(array.popleft())

print(*array)
