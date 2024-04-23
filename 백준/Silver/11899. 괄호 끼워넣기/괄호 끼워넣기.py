S = input()
stack = []
count = 0
for i in S:
    if i == '(':
        stack.append('(')
    elif stack and '(' in stack and i == ')':
        stack.pop()
    elif not stack or i == ')':
        count += 1
print(len(stack) + count)
