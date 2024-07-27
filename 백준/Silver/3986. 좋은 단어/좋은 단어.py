result = 0
for _ in range(int(input())):
    S = input()
    stack = []
    for s in S:
        if not stack or stack[-1] != s:
            stack.append(s)
        else:
            stack.pop()

    if not stack:
        result += 1

print(result)
