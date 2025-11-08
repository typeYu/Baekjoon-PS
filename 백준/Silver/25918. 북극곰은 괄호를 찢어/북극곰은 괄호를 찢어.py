import sys
N = int(sys.stdin.readline().strip())
S = sys.stdin.readline().strip()
stack, answer = [], 0
for s in S:
    if len(stack) == 0:
        stack.append(s)
    else:
        if s == '(':
            if stack[-1] == ')':
                answer = max(answer, len(stack))
                stack.pop()
            else:
                stack.append('(')
        elif s == ')':
            if stack[-1] == ')':
                stack.append(')')
            else:
                answer = max(answer, len(stack))
                stack.pop()

if stack:
    print(-1)
else:
    print(answer)