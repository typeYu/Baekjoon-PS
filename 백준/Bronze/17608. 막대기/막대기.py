import sys
N = int(sys.stdin.readline().strip())
stack = []
for _ in range(N):
    stack.append(int(sys.stdin.readline().strip()))

result = 1
compari = stack[-1]
for i in range(len(stack) - 2, -1, -1):
    if stack[i] <= compari:
        continue
    else:
        compari = stack[i]
        result += 1

print(result)