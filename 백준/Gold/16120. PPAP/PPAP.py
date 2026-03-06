import sys
S = sys.stdin.readline().strip()
stack = []

for s in S:
    stack.append(s)

    while len(stack) >= 4 and ''.join(stack[-4:]) == "PPAP":
        for _ in range(4):
            stack.pop()
        stack.append('P')

if "A" in stack or len(stack) != 1:
    print("NP")
else:
    print("PPAP")
