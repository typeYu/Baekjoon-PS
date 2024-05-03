from collections import deque
N = int(input())
balloons = list(map(int, input().split()))
array = deque([i for i in range(1, N + 1)])
for _ in range(1, N+1):
    a = array.popleft()
    print(a, end=" ")
    if balloons[a - 1] > 0:
        array.rotate(-balloons[a - 1] + 1)
    else:
        array.rotate(-balloons[a - 1])