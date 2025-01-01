import sys
n = int(sys.stdin.readline())
array = []
for _ in range(n):
    array.append(int(sys.stdin.readline()))

arr_idx = 0
stack = []
result = []
for i in range(1, n + 1):
    if i == array[arr_idx]:
        result.append('+')
        result.append('-')
        arr_idx += 1
    else:
        result.append('+')
        stack.append(i)
    while stack:
        if array[arr_idx] == stack[-1]:
            stack.pop()
            result.append('-')
            arr_idx += 1
        else:
            break


if stack:
    print("NO")
else:
    for o in result:
        print(o)
