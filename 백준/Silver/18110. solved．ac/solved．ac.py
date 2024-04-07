from collections import deque
N = int(input())
if N == 0:
    print(0)
    exit()
def roundUp(num):
    if(num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)
Percent15 = roundUp(N * 0.15)
array = []
for _ in range(N):
    array.append(int(input()))
array.sort()
queue = deque(array)
for _ in range(Percent15):
    queue.pop()
    queue.popleft()
result = roundUp(sum(queue) / len(queue))
print(result)