import sys
from collections import deque
S = sys.stdin.readline().strip()
stack = deque()
is_sign = False
for s in S:
    if s == '<':
        is_sign = True
        stack.append('<')
    elif s == '>':
        is_sign = False
        stack.append('>')
        for st in stack:
            print(st, end='')
        stack = deque()
    elif s == ' ':
        stack.append(s)
        for st in stack:
            print(st, end='')
        stack = deque()
    else:
        if is_sign:
            stack.append(s)
        else:
            stack.appendleft(s)

for st in stack:
    print(st, end='')