import sys
from collections import deque
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split()))
a, b = map(int, sys.stdin.readline().strip().split())
a -= 1
b -= 1


def bfs():
    queue = deque([(a, 0)]) # 현재 인덱스, 현재 이동한 거리
    visited = [False] * N
    visited[a] = True

    while queue:
        q, cnt = queue.popleft()
        if q == b:
            return cnt

        jump = arr[q]
        while jump + q < N:
            if not visited[jump + q]:
                queue.append((jump + q, cnt + 1))
                visited[jump + q] = True
            jump += arr[q]

        jump = arr[q]
        while 0 <= q - jump:
            if not visited[q - jump]:
                queue.append((q - jump, cnt + 1))
                visited[q - jump] = True

            jump += arr[q]

    return -1


print(bfs())