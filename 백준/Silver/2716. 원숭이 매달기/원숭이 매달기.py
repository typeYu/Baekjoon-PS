import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    array = sys.stdin.readline().strip()
    if array == '':
        print(1)
        continue

    depth = 0
    max_depth = 0
    for a in array:
        if a == '[':
            depth += 1
            max_depth = max(max_depth, depth)
        elif a == ']':
            depth -= 1

    print(2 ** max_depth)