import sys
N = int(sys.stdin.readline())
array = [int(sys.stdin.readline()) for _ in range(N)]

stack, result = [], 0
for i in array:
    while stack:
        if stack[-1] > i:
            result += len(stack)
            break
        else:
            stack.pop()
    stack.append(i)

print(result)