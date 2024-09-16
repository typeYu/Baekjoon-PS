import sys
N = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().strip().split()))

stack, result = [], [-1] * N
for index, num in enumerate(array):
    while stack:
        if stack[-1][1] < num:
            i, n = stack.pop()
            result[i] = num
        else:
            break
    stack.append([index, num])

print(*result)