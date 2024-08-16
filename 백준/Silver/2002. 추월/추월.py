from collections import deque
N = int(input())
before, after = deque([]), deque([])
for _ in range(N):
    before.append(input())
for _ in range(N):
    after.append(input())

result = 0
while before:
    if before[0] != after[0]:
        before.remove(after[0])
        result += 1
        after.popleft()
    else:
        before.popleft()
        after.popleft()

print(result)