import sys
from collections import deque
N = int(sys.stdin.readline())
router = deque()

while True:
    info = int(sys.stdin.readline())
    if info == -1:
        break
    elif info == 0:
        router.popleft()
    else:
        if len(router) == N:
            continue
        else:
            router.append(info)

if len(router) == 0:
    print("empty")
else:
    print(*router)