stack = []
for _ in range(int(input())):
    stack.append(int(input()))

stack.sort()
print(*stack, sep='\n')