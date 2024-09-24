import sys
N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().strip().split()))

result = [-1] * N
stack = []
for index, num in enumerate(array, start = 1):
    while stack:
        if stack[-1][1] == num:
            break
        else:
            i, n = stack.pop()
            result[i - 1] = index
    stack.append([index, num])

print(*result)