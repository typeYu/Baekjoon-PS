import heapq
import sys

for _ in range(int(sys.stdin.readline())):
    heap1 = [] # 최솟값 구하는 힙
    heap2 = [] # 최댓값 구하는 힙(-를 붙여서 넣어줌)
    visited = {}

    k = int(sys.stdin.readline())
    for _ in range(k):
        s, n = map(str, sys.stdin.readline().strip().split())
        n = int(n)

        if s == 'I':
            heapq.heappush(heap1, n)
            heapq.heappush(heap2, -n)
            if n in visited:
                visited[n] += 1
            else:
                visited[n] = 1

        elif s == 'D':
            if n == -1:
                while len(heap1) > 0:
                    p = heapq.heappop(heap1)
                    if visited[p] != 0:
                        visited[p] -= 1
                        break
            elif n == 1:
                while len(heap2) > 0:
                    p = heapq.heappop(heap2)
                    if visited[-p] != 0:
                        visited[-p] -= 1
                        break

    while len(heap2) > 0:
        p = heapq.heappop(heap2)
        if visited[-p] != 0:
            print(-p, end=' ')
            break

    else:
        print("EMPTY")
        continue

    while len(heap1) > 0:
        p = heapq.heappop(heap1)
        if visited[p] != 0:
            print(p)
            break
