import sys
import heapq
for _ in range(int(sys.stdin.readline())):
    M = int(sys.stdin.readline())
    answer = []
    queue1, queue2 = [], []
    for _ in range(M // 10 + 1):
        S = list(map(int, sys.stdin.readline().strip().split()))
        for i in range(len(S)):
            current = S[i]
            if len(queue1) == 0:
                heapq.heappush(queue1, -current)
            else:
                num = -(heapq.heappop(queue1))
                if num < current:
                    heapq.heappush(queue1, -num)
                    heapq.heappush(queue2, current)
                else:
                    heapq.heappush(queue1, -current)
                    heapq.heappush(queue2, num)

            if len(queue1) < len(queue2):
                q = heapq.heappop(queue2)
                heapq.heappush(queue1, -q)

            if i % 2 == 0:
                mid = heapq.heappop(queue1)
                answer.append(-mid)
                heapq.heappush(queue1, mid)

    n = len(answer)
    print(n)
    for i in range(0, len(answer), 10):
        print(*answer[i:i + 10])
