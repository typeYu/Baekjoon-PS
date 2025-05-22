import sys
import heapq
N = int(sys.stdin.readline())
left, right = [], []

for _ in range(N):
    num = int(sys.stdin.readline())

    if len(left) == len(right):
        heapq.heappush(left, -num) # 작은 수들이 모여있는 배열에서 제일 큰 수를 빼내기 위해서
    else:
        heapq.heappush(right, num) # 큰 수들이 모여있는 배열에서 작은 수를 빼내기 위해서

    if right and -left[0] > right[0]:
        num1 = -(heapq.heappop(left))
        num2 = heapq.heappop(right)

        heapq.heappush(right, num1)
        heapq.heappush(left, -num2)

    print(-(left[0]))