import sys
N = int(sys.stdin.readline().strip())
tower = list(map(int, sys.stdin.readline().strip().split()))

stack = []
result = [0] * N
for index, height in enumerate(tower):
    while stack:
        if stack[-1][1] < height:
            stack.pop()
        else:
            result[index] = stack[-1][0] + 1
            break
    stack.append([index, height])

print(*result)